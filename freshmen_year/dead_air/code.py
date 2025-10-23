# Radio scanner that searches through channels
channel_num = 0
decoded_key = ""
captured_keys = []  
result_word = ""

def continuous_scan():
    global channel_num
    radio.set_group(channel_num)
    channel_num += 1
    if channel_num > 254:  # Reset when reaching max
        channel_num = 0
    basic.pause(1500)  # Longer pause between scans
basic.forever(continuous_scan)

def handle_received_message(incoming_message):
    global captured_keys
    global result_word
    result_word = ""
    decoded_key = incoming_message
    
    # Skip if we've seen this key before
    if incoming_message not in captured_keys:
        captured_keys.append(incoming_message)
        
        # ROT13 decryption process
        for char_index in range(0, len(decoded_key)):
            current_char = decoded_key[char_index]
            ascii_value = current_char.charCodeAt(0)
            normalized = ascii_value - 97  # Shift to 0-based range
            rotated = normalized + 13     # Apply ROT13
            wrapped = (rotated % 26)      # Handle wraparound
            new_ascii = wrapped + 97      # Convert back to ASCII
            decoded_char = String.from_char_code(new_ascii)
            result_word += decoded_char
            
        print("Decoded word: " + result_word)
        basic.show_string(result_word)
    else:
        print("Key found already")
        basic.show_icon(IconNames.NO)
        
radio.on_received_string(handle_received_message)

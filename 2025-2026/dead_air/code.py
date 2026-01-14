channel = 0
foundKey = ""
data: List[str] = []  
word = ""

def on_forever(): # code for radio scanning. (should work)
    global channel
    print("channel scanned: " + channel)

    radio.set_group(channel) # sets radio group to the channel variable
    channel += 1 # adds a increment of 1 for the channel        
    if channel >= 255: # resets channel placement
        channel = 0
    basic.pause(1000)
    
basic.forever(on_forever)  

def on_received_string(receivedString):
    global word
    global data
    word = ""
    foundKey = receivedString # matches key with string
    matches = 0
    if receivedString not in data:
        data.append(receivedString) 
        for i in range(0, len(foundKey)): # decrypts the key 
            character = foundKey[i]
            ASCIIValue = character.charCodeAt(0)
            newRangeValue = ASCIIValue - 97
            introduceShift = newRangeValue + 13
            solveWrapAround = (introduceShift % 26)
            newASCIIValue = solveWrapAround + 97
            decodedCharacter = String.from_char_code(newASCIIValue)
            word = word + decodedCharacter
        print("encoded word: " + receivedString)
        print("decoded word: " + word)
    
        basic.show_string(word)
    else:
        print("key found already") # says if key is already in array (key found already)
        basic.show_icon(IconNames.NO)
radio.on_received_string(on_received_string)

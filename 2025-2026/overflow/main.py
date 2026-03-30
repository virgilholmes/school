# overflow - virgilholmes
light_list = []
max_val = 0
best_angle = 0

pins.analog_set_period(AnalogPin.P0, 20000)

def on_button_pressed_a():
    global light_list, max_val, best_angle
    light_list = []
    max_val = 0
    best_angle = 0
    for i in range(181):
    
        pins.servo_write_pin(AnalogPin.P0, i)
        
        pause(40)
        current_voltage = (pins.analog_read_pin(AnalogPin.P0) + pins.analog_read_pin(AnalogPin.P1))/2
        print("current volt: " + current_voltage)
        light_list.append(current_voltage)

    for i in range(len(light_list)):
        if light_list[i] > max_val:
            max_val = light_list[i]
            best_angle = i

    pins.servo_write_pin(AnalogPin.P0, best_angle)
    print("best angle found! " + best_angle + " degrees")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pins.servo_write_pin(AnalogPin.P0, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

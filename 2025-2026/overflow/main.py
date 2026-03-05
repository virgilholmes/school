# overflow project code - virgilholmes 
def on_forever():
  for i in range(181): #spinny thing
    pins.servo_write_pin(AnalogPin.P0,i)
    basic.pause(40)
  pins.servo_write_pin(AnalogPin.P0,0)
  basic.pause(1000)
basic.forever(on_forever)


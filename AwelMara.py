import RPi.GPIO as GPIO
import time
from RPLCD.gpio import CharLCD

# Set up GPIO mode
GPIO.setmode(GPIO.BOARD)

# Set up pins
PIR_sensor1 = 14
PIR_sensor2 = 15
m11 = 0
m12 = 1
ledRed = 2
ledGreen = 4
ledOrange = 3
ledWhite = 5
buzzer = 6
buttonPin = 7

# Set up LCD
lcd = CharLCD(pin_rs=13, pin_rw=12, pin_e=11, pins_data=[10, 9, 8], numbering_mode=GPIO.BOARD, cols=16, rows=2)

# Configure GPIO pins
GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.setup(ledOrange, GPIO.OUT)
GPIO.setup(ledWhite, GPIO.OUT)
GPIO.setup(PIR_sensor1, GPIO.IN)
GPIO.setup(PIR_sensor2, GPIO.IN)
GPIO.setup(buttonPin, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

def setup():
    lcd.write_string("    Automatic    ")
    lcd.cursor_pos = (1, 0)
    lcd.write_string("   Gate Opener   ")
    time.sleep(3)
    lcd.clear()
    lcd.write_string("Khaled Gate")
    time.sleep(2)
    GPIO.output(ledWhite, GPIO.HIGH)

def loop():
    while True:
        if GPIO.input(PIR_sensor1) or GPIO.input(buttonPin):
            lcd.clear()
            lcd.write_string(" Detect Movement ")
            lcd.cursor_pos = (1, 0)
            lcd.write_string("    Gate Opening    ")
            GPIO.output(m11, GPIO.HIGH)
            GPIO.output(m12, GPIO.LOW)
            GPIO.output(ledRed, GPIO.LOW)
            GPIO.output(ledOrange, GPIO.LOW)
            GPIO.output(ledWhite, GPIO.LOW)
            GPIO.output(ledGreen, GPIO.HIGH)
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(10)
            lcd.clear()

            lcd.write_string("   Detect motion   ")
            GPIO.output(m11, GPIO.LOW)
            GPIO.output(m12, GPIO.LOW)
            GPIO.output(ledRed, GPIO.LOW)
            GPIO.output(ledGreen, GPIO.LOW)
            GPIO.output(buzzer, GPIO.LOW)
            GPIO.output(ledOrange, GPIO.HIGH)
            time.sleep(5)
            lcd.clear()

        if GPIO.input(PIR_sensor2):
            lcd.write_string("   Gate Closing    ")
            GPIO.output(m11, GPIO.LOW)
            GPIO.output(m12, GPIO.HIGH)
            GPIO.output(ledGreen, GPIO.LOW)
            GPIO.output(ledOrange, GPIO.LOW)
            GPIO.output(ledWhite, GPIO.LOW)
            GPIO.output(ledRed, GPIO.HIGH)
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(10)
            lcd.clear()

            lcd.write_string("   Gate Closed    ")
            GPIO.output(m11, GPIO.LOW)
            GPIO.output(m12, GPIO.LOW)
            GPIO.output(buzzer, GPIO.LOW)

if __name__ == "__main__":
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        lcd.clear()
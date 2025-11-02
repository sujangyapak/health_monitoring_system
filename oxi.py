import lcd_drivers
from time import sleep
import max30100

display = lcd_drivers.Lcd()

mx30 = max30100.MAX30100()
mx30.enable_spo2()

def calculate_spo2(ir, red):
    
    ratio = (ir / red)
    spo2 = 110 - 25 * ratio  

    
    
    return spo2

while True:
    mx30.read_sensor()

    ir = mx30.ir
    red = mx30.red

    if ir and red:
        hb = int(ir / 100)
        spo2 = int(calculate_spo2(ir, red))
        if hb<10:
            print("Place finger")
            display.lcd_display_string(f"Not detected", 1)
            display.lcd_display_string(f"Place finger", 2)
            
        else:
            
            print("Pulse:", hb)
            print("SPO2:", int(spo2))
            display.lcd_clear()
            display.lcd_display_string(f"Pulse:{int(hb)}", 1)
            display.lcd_display_string(f"SpO2:{int(spo2)}%", 2) 
    else:
        print("wait")
    sleep(2)


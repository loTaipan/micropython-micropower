# alarm.py Demonstrate using RTC alarms to exit pyb.standby()

# Copyright Peter Hinch
# V0.3 13th February 2016
# Flashes leds at 30 second intervals courtesy of two concurrent timers
# (each times out at one minute intervals).
# Note that the Pyboard flashes the green LED briefly on waking from standby.
import stm, pyb, upower

red, green, yellow, blue = (pyb.LED(x) for x in range(1, 5))
rtc = pyb.RTC()
rtc.wakeup(None) # If we have a backup battery clear down any setting from a previously running program
reason = upower.why()                           # Why have we woken?
if reason == 'BOOT':                            # first boot
    rtc.datetime((2015, 8, 6, 4, 13, 0, 0, 0))  # Code to run on 1st boot only
    aa = upower.Alarm('a')
    aa.timeset(second = 39)
    ab = upower.Alarm('b')
    ab.timeset(second = 9)
    red.on()
elif reason == 'POWERUP':                       # Backup battery in place
    blue.on()
elif reason == 'ALARM_A':
    green.on()
elif reason == 'ALARM_B':
    yellow.on()

upower.lpdelay(1000)     # Let LED's be seen!
pyb.standby()

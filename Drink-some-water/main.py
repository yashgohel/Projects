import time
from plyer import notification

while True:
    notification.notify(title="Please drink some water!", message="You need to drink some water now!")
    time.sleep(5) #You need to write time in terms of second inside time.sleep()
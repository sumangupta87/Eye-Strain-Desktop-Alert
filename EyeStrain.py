# @Suman Gupta, sumangupta87@gmail.com
# Eye Strain Alert!!


from plyer import notification
import time

def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 10,
        )

while True:
    notifyMe('Eye Strain Alert!!','Take a 20 sec Break(Rule 20-20-20) from Digital screen..')
    time.sleep(1220)
    

from Drone import Drone
import time
##drone=Drone('192.168.4.1',23)
##drone.Connect()
##drone.Arm()
##drone.setThrottle(1000)       #ThrottleLow-1000,ThrottleHigh-2000
#drone.setRoll()              #RollLow-1200(Left),RollHigh(Right)-1800
#drone.SetPitch()             #Pitchlow-1200,PitchHigh-1800
#drone.SetYaw()               #YawLow(Left)-1000,YawHigh(Right)-2000
#drone.Disarm()

##while 0==0:
##    drone.setThrottle(2000)
##    time.sleep(2)
##    drone.setRoll(1200)
##    time.sleep(1)
##    drone.setThrottle(2000)
##    time.sleep(5)
##    drone.SetPitch(1800)
##    time.sleep(5)
##    
##    break
##
##drone.Disarm()    
##drone.closeConnection()

drone=Drone('192.168.4.1',23)
drone.Connect()
drone.Arm()
drone.setThrottle(1000)
while 0 == 0:
  drone.setThrottle(2000)
  time.sleep(5)
  drone.setRoll(1200)
  time.sleep(1)
  drone.SetPitch(1800)
  time.sleep(2)
  drone.SetYaw(1800)
  time.sleep(5)
  break
drone.Disarm()
drone.closeConnection()

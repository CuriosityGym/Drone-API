import socket
import time, math

class drone:
    def getBytes(self,value): 
        self.LSB=value % 256
        self.MSB=math.floor(value/256)
        return bytearray([self.LSB,self.MSB])
    
    def connect(self):
        self.headerArray=bytearray([36,77,60])
        self.valueArray=bytearray([])
        self.roll=1500                    
        self.pitch=1500                 
        self.throttle=1500 
        self.yaw=1500                      
        self.aux1=1200
        self.aux2=1000
        self.aux3=1500
        self.aux4=1200      
        self.valueArray.extend(self.headerArray)
        self.valueArray.append(16)
        self.valueArray.append(200)
        self.valueArray.extend(drone.getBytes(self.roll))
        self.valueArray.extend(drone.getBytes(self.pitch))
        self.valueArray.extend(drone.getBytes(self.throttle))
        self.valueArray.extend(drone.getBytes(self.yaw))
        self.valueArray.extend(drone.getBytes(self.aux1))
        self.valueArray.extend(drone.getBytes(self.aux2))
        self.valueArray.extend(drone.getBytes(self.aux3))
        self.valueArray.extend(drone.getBytes(self.aux4))
        self.CRCArray=self.valueArray[3:]
        self.CRCValue=0
        for d in self.CRCArray:
        	self.CRCValue= self.CRCValue^d
        self.valueArray.append(self.CRCValue)
        return self.valueArray

    def arm(self):
        self.headerArray=bytearray([36,77,60])
        self.valueArray=bytearray([])
        self.roll=1500                   
        self.pitch=1500                 
        self.throttle=1500
        self.yaw=1500                      
        self.aux1=1200
        self.aux2=1000
        self.aux3=1500
        self.aux4=1500       #Change
        self.valueArray.extend(self.headerArray)
        self.valueArray.append(16)
        self.valueArray.append(200)
        self.valueArray.extend(drone.getBytes(self.roll))
        self.valueArray.extend(drone.getBytes(self.pitch))
        self.valueArray.extend(drone.getBytes(self.throttle))
        self.valueArray.extend(drone.getBytes(self.yaw))
        self.valueArray.extend(drone.getBytes(self.aux1))
        self.valueArray.extend(drone.getBytes(self.aux2))
        self.valueArray.extend(drone.getBytes(self.aux3))
        self.valueArray.extend(drone.getBytes(self.aux4))
        self.CRCArray=self.valueArray[3:]
        self.CRCValue=0
        for d in self.CRCArray:
        	self.CRCValue= self.CRCValue^d
        self.valueArray.append(self.CRCValue)
        return self.valueArray

    def Disarm(self):
        self.headerArray=bytearray([36,77,60])
        self.valueArray=bytearray([])
        self.roll=1500                  
        self.pitch=1500                
        self.throttle=1500
        self.yaw=1500                      
        self.aux1=1200
        self.aux2=1000
        self.aux3=1500
        self.aux4=1200       #Change
        self.valueArray.extend(self.headerArray)
        self.valueArray.append(16)
        self.valueArray.append(200)
        self.valueArray.extend(drone.getBytes(self.roll))
        self.valueArray.extend(drone.getBytes(self.pitch))
        self.valueArray.extend(drone.getBytes(self.throttle))
        self.valueArray.extend(drone.getBytes(self.yaw))
        self.valueArray.extend(drone.getBytes(self.aux1))
        self.valueArray.extend(drone.getBytes(self.aux2))
        self.valueArray.extend(drone.getBytes(self.aux3))
        self.valueArray.extend(drone.getBytes(self.aux4))
        self.CRCArray=self.valueArray[3:]
        self.CRCValue=0
        for d in self.CRCArray:
        	self.CRCValue= self.CRCValue^d
        self.valueArray.append(self.CRCValue)
        return self.valueArray
    
    def setThrottle(self,value):
        self.headerArray=bytearray([36,77,60])
        self.valueArray=bytearray([])
        self.roll=1500                 
        self.pitch=1500                 
        self.throttle=value #Change
        self.yaw=1500                      
        self.aux1=1200
        self.aux2=1000
        self.aux3=1500
        self.aux4=1500      
        self.valueArray.extend(self.headerArray)
        self.valueArray.append(16)
        self.valueArray.append(200)
        self.valueArray.extend(drone.getBytes(self.roll))
        self.valueArray.extend(drone.getBytes(self.pitch))
        self.valueArray.extend(drone.getBytes(self.throttle))
        self.valueArray.extend(drone.getBytes(self.yaw))
        self.valueArray.extend(drone.getBytes(self.aux1))
        self.valueArray.extend(drone.getBytes(self.aux2))
        self.valueArray.extend(drone.getBytes(self.aux3))
        self.valueArray.extend(drone.getBytes(self.aux4))
        self.CRCArray=self.valueArray[3:]
        self.CRCValue=0
        for d in self.CRCArray:
        	self.CRCValue= self.CRCValue^d
        self.valueArray.append(self.CRCValue)
        return self.valueArray
    
    def setRoll(self,value):
        self.headerArray=bytearray([36,77,60])
        self.valueArray=bytearray([])
        self.roll=value  #Change                
        self.pitch= 1500               
        self.throttle=1500
        self.yaw=1500                      
        self.aux1=1200
        self.aux2=1000
        self.aux3=1500
        self.aux4=1500      
        self.valueArray.extend(self.headerArray)
        self.valueArray.append(16)
        self.valueArray.append(200)
        self.valueArray.extend(drone.getBytes(self.roll))
        self.valueArray.extend(drone.getBytes(self.pitch))
        self.valueArray.extend(drone.getBytes(self.throttle))
        self.valueArray.extend(drone.getBytes(self.yaw))
        self.valueArray.extend(drone.getBytes(self.aux1))
        self.valueArray.extend(drone.getBytes(self.aux2))
        self.valueArray.extend(drone.getBytes(self.aux3))
        self.valueArray.extend(drone.getBytes(self.aux4))
        self.CRCArray=self.valueArray[3:]
        self.CRCValue=0
        for d in self.CRCArray:
        	self.CRCValue= self.CRCValue^d
        self.valueArray.append(self.CRCValue)
        return self.valueArray
    
    def setPitch(self,value):
        self.headerArray=bytearray([36,77,60])
        self.valueArray=bytearray([])
        self.roll=1500                 
        self.pitch=value #Change               
        self.throttle=1500
        self.yaw=1500                      
        self.aux1=1200
        self.aux2=1000
        self.aux3=1500
        self.aux4=1500       
        self.valueArray.extend(self.headerArray)
        self.valueArray.append(16)
        self.valueArray.append(200)
        self.valueArray.extend(drone.getBytes(self.roll))
        self.valueArray.extend(drone.getBytes(self.pitch))
        self.valueArray.extend(drone.getBytes(self.throttle))
        self.valueArray.extend(drone.getBytes(self.yaw))
        self.valueArray.extend(drone.getBytes(self.aux1))
        self.valueArray.extend(drone.getBytes(self.aux2))
        self.valueArray.extend(drone.getBytes(self.aux3))
        self.valueArray.extend(drone.getBytes(self.aux4))
        self.CRCArray=self.valueArray[3:]
        self.CRCValue=0
        for d in self.CRCArray:
        	self.CRCValue= self.CRCValue^d
        self.valueArray.append(self.CRCValue)
        return self.valueArray

    def setYaw(self,value):
        self.headerArray=bytearray([36,77,60])
        self.valueArray=bytearray([])
        self.roll=1500                 
        self.pitch=1500               
        self.throttle=1500
        self.yaw=value #Change                     
        self.aux1=1200
        self.aux2=1000
        self.aux3=1500
        self.aux4=1500       
        self.valueArray.extend(self.headerArray)
        self.valueArray.append(16)
        self.valueArray.append(200)
        self.valueArray.extend(drone.getBytes(self.roll))
        self.valueArray.extend(drone.getBytes(self.pitch))
        self.valueArray.extend(drone.getBytes(self.throttle))
        self.valueArray.extend(drone.getBytes(self.yaw))
        self.valueArray.extend(drone.getBytes(self.aux1))
        self.valueArray.extend(drone.getBytes(self.aux2))
        self.valueArray.extend(drone.getBytes(self.aux3))
        self.valueArray.extend(drone.getBytes(self.aux4))
        self.CRCArray=self.valueArray[3:]
        self.CRCValue=0
        for d in self.CRCArray:
        	self.CRCValue= self.CRCValue^d
        self.valueArray.append(self.CRCValue)
        return self.valueArray 
    
    

TCP_IP = '192.168.4.1'
TCP_PORT = 23
BUFFER_SIZE = 1024
drone=drone()

setThrottle=drone.setThrottle(1000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(setThrottle)
data = s.recv(BUFFER_SIZE)

print (data)
time.sleep(5)
print('Throttle = 0')

setThrottle=drone.setThrottle(2000)
while 1:
        s.send(setThrottle)
        data = s.recv(BUFFER_SIZE)
        print (data)
#print(valueArray)    

s.close()

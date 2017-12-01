import socket
import time, math

def getBytes(value): 
        LSB=value % 256
        MSB=math.floor(value/256)
        return bytearray([LSB,MSB])

def packetDroneON():
	headerArray=bytearray([36,77,60])
	valueArray=bytearray([])
	roll=1500
	pitch=1500
	yaw=1003        #Change
	throttle=1500
	aux1=1200
	aux2=1000
	aux3=1500
	aux4=1500           #Change
	valueArray.extend(headerArray)
	valueArray.append(16)
	valueArray.append(200)
	valueArray.extend(getBytes(roll))
	valueArray.extend(getBytes(pitch))
	valueArray.extend(getBytes(yaw))
	valueArray.extend(getBytes(throttle))
	valueArray.extend(getBytes(aux1))
	valueArray.extend(getBytes(aux2))
	valueArray.extend(getBytes(aux3))
	valueArray.extend(getBytes(aux4))
	CRCArray=valueArray[3:]
	CRCValue=0
	for d in CRCArray:
		CRCValue= CRCValue^d
	valueArray.append(CRCValue)
	return valueArray

def packet2():
	headerArray=bytearray([36,77,60])
	valueArray=bytearray([])
	roll=1500
	pitch=1500
	yaw=1500
	throttle=1490
	aux1=1200
	aux2=1000
	aux3=1500
	aux4=1200
	valueArray.extend(headerArray)
	valueArray.append(00)
	valueArray.append(108)
	CRCArray=valueArray[3:]
	CRCValue=0
	for d in CRCArray:
		CRCValue= CRCValue^d
	valueArray.append(CRCValue)
	return valueArray

def packet3():
	headerArray=bytearray([36,77,60])
	valueArray=bytearray([])
	roll=1500
	pitch=1500
	yaw=1500
	throttle=1490
	aux1=1200
	aux2=1000
	aux3=1500
	aux4=1200
	valueArray.extend(headerArray)
	valueArray.append(00)
	valueArray.append(110)
	CRCArray=valueArray[3:]
	CRCValue=0
	for d in CRCArray:
		CRCValue= CRCValue^d
	valueArray.append(CRCValue)
	return valueArray

def packet4():
	headerArray=bytearray([36,77,60])
	valueArray=bytearray([])
	roll=1500
	pitch=1500
	yaw=1500
	throttle=1490
	aux1=1200
	aux2=1000
	aux3=1500
	aux4=1200
	valueArray.extend(headerArray)
	valueArray.append(00)
	valueArray.append(255)
	CRCArray=valueArray[3:]
	CRCValue=0
	for d in CRCArray:
		CRCValue= CRCValue^d
	valueArray.append(CRCValue)
	return valueArray


TCP_IP = '192.168.4.1'
TCP_PORT = 23
BUFFER_SIZE = 1024

packetDroneON=packetDroneON()
packet2=packet2()
packet3=packet3()
packet4=packet4()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


while 1:
        s.send(packetDroneON)
        data = s.recv(BUFFER_SIZE)
        print (data)
        s.send(packet2)
        data = s.recv(BUFFER_SIZE)
        print (data)
        s.send(packet3)
        data = s.recv(BUFFER_SIZE)
        print (data)
        s.send(packet4)
        data = s.recv(BUFFER_SIZE)
        print (data)
#print(valueArray)    

s.close()

import serial 
import time
import datetime
import logging
ser = serial.Serial('COM10', 9600, timeout=30)
#target = open("data_from_sensors.txt", 'w')
logging.basicConfig(filename='data_from_sensors.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
#logging.info('So should this')

with open("data_from_sensors.txt", 'w') as file1:
 print "Format: Temp_from_SHT31 : Temp_from_DS180B20_1 : Temp_from_DS180B20_2 : Humidity_from_SHT31 : Humidity_from_dht22 : Temp_from_dht22"
 zee = "Format: Temp_from_SHT31 : Temp_from_DS180B20+1 : Temp_from_DS180B20_2 : Humidity_from_SHT31 : Humidity_from_dht22 : Temp_from_dht22"
 logging.info(zee)
 file1.write(zee)
 while 1:
 	try:
  		a = ser.readline()
  		print datetime.datetime.now(), " : " ,a
  		b = datetime.datetime.strftime(datetime.datetime.now(),"%d-%m-%Y %H:%M:%S") + " : "  + str(a)
  		#print a
  		file1.write(b)
  		logging.info(b)
  		time.sleep(1)
 	except:
  		print('Data could not be read')
 	time.sleep(1)
 




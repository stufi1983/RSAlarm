#!/usr/bin/env python2
import time
import serial
import mysql.connector
import datetime
from datetime import datetime
cars = ["L", "L","L", "L","L", "L","L", "L"]
from mysql.connector import Error

def areEqual(arr1, arr2, n, m, equalval): 
  
    # If lengths of array are not  
    # equal means array are not equal 
    if (n != m): 
        return False; 
  
    # Sort both arrays 
    if equalval:
        arr1.sort(); 
        arr2.sort(); 
  
    # Linearly compare elements 
    for i in range(0, n - 1): 
        if (arr1[i] != arr2[i]): 
            return False; 
  
    # If all elements were same. 
    return True; 
    
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='antrianku',
                                         user='root',
                                         password='winda1984')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)
    
bed = 0
serialcmd = "AT\r\n"
connected = False

ser = serial.Serial('/dev/ttyS0', baudrate=1200,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
time.sleep(1)
try:
    print ("Starting Program")
    ser.write(serialcmd.encode())
    while True:
        #time.sleep(1)
        carsnow = ["H", "H","H", "H","H", "H","H", "H"]
            
        try:
            connection = mysql.connector.connect(host='localhost',
                                         database='antrianku',
                                         user='root',
                                         password='winda1984')
            if connection.is_connected():
                cekroom = "SELECT room FROM bedevents INNER JOIN bedmap ON bedevents.bed_id = bedmap.bed WHERE status = 'START' GROUP BY room"
                cursor = connection.cursor()
                cursor.execute(cekroom)
                records = cursor.fetchall()
                #print(records)
                for row in records:
                    carsnow[row[0]-1] = "L"

                    
                if not areEqual(cars,carsnow,len(cars),len(carsnow),False):
                    print("Update switch")
                    for i in range(0, len(cars) - 1): 
                        if carsnow[i] == "L":
                            sendstring = "L{}\r\n".format(i)
                        if carsnow[i] == "H":
                            sendstring = "H{}\r\n".format(i)
                        ser.write(sendstring.encode())
                        print(sendstring)
                        cars[i] = carsnow[i]
                        
                    

        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                #print("MySQL connection is closed")
        
        if ser.inWaiting() > 0:
            data = ser.readline()
            print (data)

            if data[0]==79 and data[1]==75: #79--> 0, 75 --> K
                print ('Connected')
                connected = True
            #if connected != True:
                #ser.write(serialcmd.encode())
                #continue
            if data[0]==82: #82--> R
                bed = (data[1] - 0x30 + 1)
                print ("Bed: ",bed)
                
                print("Is any data already?")
                try:
                    connection = mysql.connector.connect(host='localhost',
                                         database='antrianku',
                                         user='root',
                                         password='winda1984')
                    if connection.is_connected():
                        triggerbed = "SELECT bed_id FROM bedevents INNER JOIN bedmap ON bedevents.bed_id = bedmap.bed WHERE status = 'START' AND bed = '{}'".format(bed)
                        cursor = connection.cursor()
                        cursor.execute(triggerbed)
                        record = cursor.fetchone()
                except Error as e:
                    print("Error while connecting to MySQL", e)
                finally:
                    if (connection.is_connected()):
                        cursor.close()
                        connection.close()
                        #print("MySQL connection is closed")
        
                if record != None:
                    print("Already")
                if record == None:
                    print ("No. Insert data")
                    try:
                        connection = mysql.connector.connect(host='localhost',
                                         database='antrianku',
                                         user='root',
                                         password='winda1984')
                        if connection.is_connected():
                            insertstr = "INSERT INTO `bedevents` (`id`, `trigger_time`, `bed_id`, `status`, `stop_time`) VALUES ('', '{}', '{}', 'START', NULL)".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),bed)
                            #print(insertstr)
                            cursor = connection.cursor()
                            cursor.execute(insertstr)
                            connection.commit()
                            print("Done")
                    except Error as e:
                        print("Error while connecting to MySQL", e)
                    finally:
                        if (connection.is_connected()):
                            cursor.close()
                            connection.close()
                            #print("MySQL connection is closed")
        
except KeyboardInterrupt:
    print ("Exiting Program")

except:
    print ("Error Occurs, Exiting Program")

finally:
    ser.close()
    pass

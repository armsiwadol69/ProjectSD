import serial
import MySQLdb
import time
import aqi
import sys
print("Sending PM1.0 PM2.5 PM10.0 Data to MySQL Server")
print("SDPJ By Siwadol M. DM6201")
count = 0
def conn():
    print("Phase 2 : Connecting To Database")
    dbConn = MySQLdb.connect("sql417.main-hosting.eu", "u584979650_siwadol", "@Siwadol420", "u584979650_si_sd") or die("could not connect to database")
    # open a cursor to the database
    cursor = dbConn.cursor()
    print("OK!")
    cursor.execute("INSERT INTO dust (pm10,pm25,pm100,date,aqi) VALUES (%s,%s,%s,%s,%s)", (pieces[0] , pieces[1], pieces[2], timestamp, aqi))
    dbConn.commit()  # commit the insert
    cursor.close()  # close the cursor
    
while True:
    device = "COM3"  # this will have to be changed to the serial port you are using
    print("Phase 1 : Receive Data From Arduino")
    try:
        print("Trying...", device)
        arduino = serial.Serial(device, 9600)
        print("Connected at ",arduino.portstr)
    except:
        print("Failed to connect on", device, "Retrying...")
        
    data = arduino.readline()  # read the data from the arduino
    print(data)
    print("decode to UTF-8")
    print(data.decode("utf-8"))
    data2 = str(data.decode("utf-8"))
    timestamp = str(time.strftime('%Y-%m-%d %H:%M:%S'))
    pieces = data2.split(" ")  # split the data by the tab
    aqi = aqi.to_iaqi(aqi.POLLUTANT_PM25, pieces[1], algo=aqi.ALGO_EPA)
    conn() #submit to mysql
    print("PM1.0 : ",pieces[0],"  PM2.5 : ",pieces[1],"  PM10.0 : ",pieces[2],"  AQI : ",aqi)
    print("Submit Time : " + timestamp)
    count = count + 1
    #print("Count : ",count," Chin | ",count/10," Chinchin | ",count/100," Zhu")
    print("DATA SUBMITTED")
    arduino.close() #close port
    print("Port", device ,"Closed")
    #print("Clsoe in 10 sec")
    print("------------------------------------------------------")
    time.sleep(10)
    sys.exit()

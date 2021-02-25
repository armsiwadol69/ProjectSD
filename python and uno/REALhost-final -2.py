import serial
import MySQLdb
import time
print("Sending DHT11 Data to MySQL Server")
print("By Siwadol M. DM6201")
def conn():
    print("Phase 2 : Connecting To Database")
    dbConn = MySQLdb.connect("sql417.main-hosting.eu", "u584979650_siwadol", "@Siwadol420", "u584979650_si_sd") or die("could not connect to database")
    # open a cursor to the database
    cursor = dbConn.cursor()
    print("OK!")
    cursor.execute("INSERT INTO rec_used (humi,temp,date) VALUES (%s,%s,%s)", (pieces[0], pieces[1], timestamp))
    dbConn.commit()  # commit the insert
    cursor.close()  # close the cursor

while True:
    device = "COM3"  # this will have to be changed to the serial port you are using
    print("Phase 1 : Receive Data From Arduino")
    try:
        print("Trying...", device)
        arduino = serial.Serial(device, 9600)
    except:
        print("Failed to connect on", device, "Retrying...")

    data = arduino.readline()  # read the data from the arduino
    print(data)
    print("decode to UTF-8")
    print(data.decode("utf-8"))
    data2 = data.decode("utf-8")
    timestamp = str(time.strftime('%Y-%m-%d %H:%M:%S'))
    pieces = data2.split(" ")  # split the data by the tab

    conn() #submit to mysql
    print("Temp : "+ pieces[1] + "\n" + "Humi : "+pieces[0]+"%")
    print("Submit Time : " + timestamp)
    print("DONE : DATA SUBMITTED")
    print("SUBMIT AGIAN IN 5 MINS")
    print("-------------------------------------------")
    time.sleep(300)

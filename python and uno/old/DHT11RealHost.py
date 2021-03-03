import serial
import MySQLdb
import time

print("Siwadol M.")
def conn():
    try:
        print("Trying...", device)
        arduino = serial.Serial(device, 9600)
    except:
        print("Failed to connect on", device)
    data = arduino.readline()  # read the data from the arduino
    print(data)
    print("decode to UTF-8")
    print(data.decode("utf-8"))
    data2 = data.decode("utf-8")
    timestamp = str(time.strftime('%Y-%m-%d %H:%M:%S'))
    print("Submit Time : " + timestamp)
    pieces = data2.split(" ")  # split the data by the tab
    cursor.execute("INSERT INTO rec_used (humi,temp,date) VALUES (%s,%s,%s)", (pieces[0], pieces[1], timestamp))
    dbConn.commit()  # commit the insert
    cursor.close()  # close the cursor

while True:
    print("Start : Connecting To Database")
    dbConn = MySQLdb.connect("sql417.main-hosting.eu", "u584979650_siwadol", "@Siwadol420", "u584979650_si_sd") or die("could not connect to database")
    # open a cursor to the database
    cursor = dbConn.cursor()
    device = "COM3"  # this will have to be changed to the serial port you are using
    conn()
    print("DONE : DATA WAS SUBMITTED TO SERVER")
    print("SUBMIT AGIAN IN 5 MINS")
    print("-------------------------------------------")
    time.sleep(5)

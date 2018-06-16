
import RPi.GPIO as GPIO
import MFRC522
import signal
import MySQLdb
import time

db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

continue_reading = True

LedPin = 11
GPIO.setmode(GPIO.BOARD)       
GPIO.setup(LedPin, GPIO.OUT)   
GPIO.output(LedPin, GPIO.LOW)

def check_worker(uid):    
    cursor = db.cursor()
    sql = "SELECT * FROM EMPLOYEE WHERE UID[0] = uid[0] AND UID[1] = uid[1] AND UID[2] = uid[2] AND UID[3] = uid[3]" 
    try: 
        results = cursor.fetchall()
        for row in results:
            driver_name = row[0]
            check_1 = row[1]
            check_2 = row[2]
            check_3 = row[3]
            check_4 = row[4]
        return driver_name
    except:
        return 0
    
    #database wala part

def send_SMS():
    #send over internet

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    (status,uid) = MIFAREReader.MFRC522_Anticoll()


    if status == MIFAREReader.MI_OK:
        print "Card detected"
        
        

    if nuid[0] != uid[0] || nuid[1] != uid[1] || nuid[2] != uid[2] || nuid[3] != uid[3]:
        nuid[0],nuid[1],nuid[2].nuid[3] = uid[0],uid[1],uid[2],uid[3]
        print "New Card Found"
        print "Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])
        name = check_worker(uid)
        if(!int(name)):
            print "Invalid Card"
        else:
            Send_SMS()
            GPIO.output(LedPin, GPIO.HIGH)  #LED replcaed by motor/pump
            time.sleep(5)
            GPIO.output(LedPin, GPIO.LOW)
    else:
        print "Card read previously"

        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        MIFAREReader.MFRC522_SelectTag(uid)
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
        if status == MIFAREReader.MI_OK:
            MIFAREReader.MFRC522_Read(8)
            MIFAREReader.MFRC522_StopCrypto1()
        else:
            print "Authentication error"

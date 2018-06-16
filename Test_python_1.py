import RPi.GPIO as GPIO
import MFRC522
import signal
import MySQLdb

db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
cursor = db.cursor()

continue_reading = True


def check_worker(uid):
    sql = "SELECT * FROM EMPLOYEE WHERE UID[0] = uid[0] AND UID[1] = uid[1] AND UID[2] = uid[2] AND UID[3] = uid[3]" 
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

        if(!name):
            print "Invalid User"
        else:
            Send_SMS()
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

import mysql.connector
from datetime import date

# Global Variables
hotel_name = ''
address = ''
phone = ''
email = ''
gst = 0
st = 0
result=''
result1=''
conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = '12345')
cursor = conn.cursor()

'''room_no = input('\n Enter Room No : ')
room_type = input('\n Enter Room Type (AC / DELUX / SUPER DELUX / QUEEN DELIGHT / KINGS SPECIAL / SUPER RICH  SPECIAL) : ')
room_rent = input('\n Enter Room Rent (INR) : ')
room_bed = input('\n Enter Room Bed Type  (SINGLE / DOUBLE / TRIPLE) : ')
print(room_no,room_type,room_rent,room_bed)'''

'''def add_room():
        clear()
        print('Add New Room - Screen')
        print('-'*120)'''
room_no = input('\n Enter Room No : ')
room_type = input('\n Enter Room Type (AC / DELUX / SUPER DELUX / QUEEN DELIGHT / KINGS SPECIAL / SUPER RICH  SPECIAL) : ')
room_rent = input('\n Enter Room Rent (INR) : ')
room_bed = input('\n Enter Room Bed Type  (SINGLE / DOUBLE / TRIPLE) : ')
sql= "insert into rooms values(%s,%s,%s,%s,'free')"
        #sql = "insert into rooms (room_no, room_type, room_rent, bed, status) values ( %s, %s, %s, %s ,'free')"
print(sql)
'''result = room_exist(room_no)
if result is None:
        cursor.execute(sql)
        
else:
        print('\n\n\n Room No', room_no, 'Already Exist In Database')'''
wait = input('\n\n\n Press Any Key To Continue..... ')



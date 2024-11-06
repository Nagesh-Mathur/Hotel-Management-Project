# Project Name : HOTEL MANAGEMENT PROJECT
# Made By : NAGESH MATHUR AND NAKSHATRA MUNSHI
# Class : 12th-A 
# Session : 2024-2025
# Subject : COMPUTER SCIENCE


import mysql.connector
from datetime import date

# Global Variables
hotel_name = ''
address = ''
phone = ''
email = ''
gst = 0
st = 0

def settings():
  global hotel_name
  global addr
  global phone
  global email
  global gst
  global st

conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = '')
cursor = conn.cursor()
sql = "select * from setting;"
cursor.execute(sql)
records = cursor.fetchall()

for record in records:
  if record[1] == 'hotel_name':
    hotel_name = record[2]
  if record[1] == 'address':
    addr = record[2]
  if record[1] == 'phone':
    phone = record[2]
  if record[1] == 'email':
    emil = record[2]
  if record[1] == 'gst':
    gst = record[2]
  if record[1] == 'st':
    st = record[2]

def system_settings():
  conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = '')
  cursor = conn.cursor()
  clear()
  print('Change System Settings')
  print('*'* 120)
  print('1.    Hotel Name')
  print('2.    Hotel Address')
  print('3.    Phone Number(s)')
  print('4.    Email Id')
  print('5.    Current GST Rate')
  print('6.    Current Service Rate')

choice = int(input("Enter Your Choice:"))
field_name = ''
if choice == 1:
  field_name = 'hotel_name'
if choice == 2:
  field_name = 'address'
if choice == 3:
  field_name = 'phone'
if choice == 4:
  field_name = 'email'
if choice == 5:
  field_name = 'gst'
if choice == 6:
  field_name = 'st'

value = input('Enter New value:')
sql = 'update setting set value = '+value+' where field_name = "'+ field_name+'";'
cursor.execute(sql)
conn.close()
wait = input('\n\n\n Record updated ................ Press Any Key To Continue........')

def clear():
  for _ in range(65):
    print()

def room_exist(room_no):
  conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = '')
  cursor = conn.cursor()
  sql = "select * from rooms where room_no = "+room_no+";"
  cursor.execute(sql)
  record = cursor.fetchone()
  return record

def customer_exist(cust_no):
  conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = '')
  cursor = conn.cursor()
  sql = "select * from customer where id = "+cust_no+";"
  cursor.execute(sql)
  record = cursor.fetchone()
  return record

def add_room():
  conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = '')
  cursor = conn.cursor()
  clear()
  print('Add New Room - Screen')
  print('-'*120)
  room_no = input('\n Enter Room No : ')
  room_type = input('\n Enter Room Type (AC / DELUX / SUPER DELUX / QUEEN DELIGHT / KINGS SPECIAL / SUPER RICH SPECIAL) : ')
  room_rent = input('\n Enter Room Rent (INR) : ')
  room_bed = input('\n Enter Room Bed Type  (SINGLE / DOUBLE / TRIPLE) : ')
  sql = 'insert into rooms (room_no, room_type, room_rent, bed, status) values ('+room_no+', "'+room_type.upper()+'", '+room_rent+', "'+room_bed.upper()+'", "free");'
  
  result = room_exist(room_no)
  if result is None:
    cursor.execute(sql)
  else:
    print('\n\n\n Room No', room_no, 'Already Exist In Database')
  conn.close()
  wait = input('\n\n\n Press Any Key To Continue..... ')

def modify_room():
  conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = '')
  cursor = conn.cursor()
  clear()
  print('Change Room Information')
  print('*'*120)
  print('1.    Room Type')
  print('2.    Room Rent')
  print('3.    Room Bed')
  choice = int(input('Enter your choice : '))
  field_name = ''
  if choice == 1:
    field_name = 'room_type'
  if choice == 2:
    field_name = 'room_rent'
  if choice == 3:
    field_name = 'room_bed'
  room_no = input('Enter Room No : ')
  value = input('Enter New Value : ')
  sql = 'update rooms set '+field_name+' = '+value+' where room_no + ';''
  cursor.execute(sql)
  wait = input('\n\n\n Record Updated ................. Press Any Key To Continue......')

def add_customer():
  

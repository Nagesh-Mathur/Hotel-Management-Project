# Project Name: HOTEL MANAGEMENT PROJECT
# Made By: NAGESH MATHUR AND NAKSHATRA MUNSHI
# Class: 12th-A 
# Session: 2024-2025
# Subject: COMPUTER SCIENCE

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





  
  

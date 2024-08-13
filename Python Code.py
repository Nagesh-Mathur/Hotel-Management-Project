# Project Name: HOTEL MANAGEMENT PROJECT
# Made By: NAGESH MATHUR AND NAKSHATRA MUNSHI
# Class: 12th-A 
# Session: 2024-2025
# Subject: COMPUTER SCIENCE

import mysql.connector
from datetime import date

# Global Variables
hotel_name=''
address=''
phone=''
email=''
gst=0
st=0

def settings():
  global hotel_name
  global address
  global phone
  global email
  global gst
  global st

conn= mysql.connector.connect( host='localhost', database='hotel', user='root', password='')
cursor= conn.cursor()
sql= "select * from setting;"
cursor.execute(sql)
records= cursor.fetchall()

for record in records:
  if record[1]=='Hotel_Name':
    hotel_name= record[2]
  if record[1]=='Address':
    address= record[2]
  if record[1]=='Phone_Number':
    phone= record[2]
  if record[1]=='Email':
    email= record[2]
  if record[1]=='GST':
    gst= record[2]
  if record[1]=='ST':
    st= record[2]
    

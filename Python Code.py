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

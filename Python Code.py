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

conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = 'Nagesh@38')
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
  conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = 'Nagesh@38')
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
  conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = 'Nagesh@38')
  cursor = conn.cursor()
  sql = "select * from rooms where room_no = "+room_no+";"
  cursor.execute(sql)
  record = cursor.fetchone()
  return record

def customer_exist(cust_no):
  conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = 'Nagesh@38')
  cursor = conn.cursor()
  sql = "select * from customer where id = "+cust_no+";"
  cursor.execute(sql)
  record = cursor.fetchone()
  return record

def add_room():
  conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = 'Nagesh@38')
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
  conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = 'Nagesh@38')
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
  conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = 'Nagesh@38')
  cursor = conn.cursor()
  clear()
  print('Add New Customer - Screen')
  print('-'*120)
  name = input('\n Enter Customer Name : ')
  address = input('\n Enter Customer Address : ')
  phone = input('\n Enter Customer Phone No : ')
  email = input('\n Enter Customer Email Id : ')
  id_proof = input('\n Enter Customer Id (Aadhar / Passport / DL / Voter Id) : ')
  id_proof_no = input('\n Enter Customer Id Proof No : ')
  males = input('\n Enter Total Males : ')
  females = input('\n Enter Total Females : ')
  children = input('\n Enter Total Children : ')
  sql = 'insert into customer(name, address, phone, email, id_proof, id_proof_no, males, females, children) values \ ("'+name+'", "'+address.upper()+'", "'+phone+'", "'+email.upper()+'", "'+id_proof.upper()+'", "'+id_proof_no.upper()+'", "'+males+'", "'+females+'", "'+children+'" )'
  cursor.execute(sql)
  print('\n\n\n Customer Added Successfully .......... ')
  conn.close()
  wait = input('\n\n\n Press Any Key To Continue ....... ')

def modify_customer():
  conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = 'Nagesh@38')
  cursor = conn.cursor()
  clear()
  print('Change Customer Information')
  print('*'*120)
  print('1.   Name')
  print('2.   Address')
  print('3.   Phone No')
  print('4.   Email Id')
  print('5.   Id Proof')
  print('6.   Id Proof No')
  print('7.   Males')
  print('8.   Females')
  print('9.   Children')
  choice = int(input('Enter Your Choice : '))
  field_name = ''
  if choice == 1:
    field_name = 'name'
  if choice == 2:
    field_name = 'address'
  if choice == 3:
    field_name = 'phone'
  if choice == 4:
    field_name = 'email'
  if choice == 5:
    field_name = 'id_proof'
  if choice == 6:
    field_name == 'id_proof_no'
  if choice == 7:
    field_name = 'males'
  if choice == 8:
    field_name = 'females'
  if choice == 9:
    field_name = 'children'
  cust_no = input('Enter Customer No : ')
  value = input('Enter New Value : ')
  sql = 'update customer set ' +field_name+ '=' +\value+ 'where id = ' +cust_no+ ';'
  cursor.execute(sql)
  wait = input('\n\n\n Record Updated ........... Press Any Key To Continue........')

def room_booking():
  conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = 'Nagesh@38')
  cursor = conn.cursor()
  room_id = input('Enter Room No To Book : ')
  cust_id = input('Enter Customer Id : ')
  check_in = input('Enter Check In Date (YYYY-MM-DD) : ')
  advance = input('Enter Advance Amount : ')
  sql1 = 'update rooms set status = "occupied" where id =' +room_id+ ';'
  sql2 = 'insert into booking (room_id, cust_id, check-in, advance) values ('+room_id+', 'cust_id', 'check_in', 'advance');'
  #print(sql2)
  #print(sql1)
  result = room_exist(room_id)
  result1 = customer_exist(cust_id)
  if result[5] == 'free' and result1 is not None :
    cursor.execute(sql1)
    cursor.execute(sql2)
    print('\n\n\n Room No', room_id, 'booked for', cust_id)
  if result[5] != 'free' :
    print('\n Room Is Not Available For Booking. Right Now It Is : ', result[5])
  if result1 is None :
    print('Customer Does Not Exist ..... Please Add Customer First in Our Database')
  conn.close()
  wait = input('\n\n\n Press Any Key To Continue.......')

def bill_generation():
  global gst
  global st
  conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = 'Nagesh@38')
  cursor = conn.cursor()
  room_id = input('Enter Room No To Book : ')
  cust_id = input('Enter Customer Id : ')
  sql = 'select * from booking where cust_id = ' +cust_id+ ' and room_id = '+room_id+' and check_out is NULL;'
  cursor.execute(sql)
  record = cursor.fetchone()
  clear()
  print('Bill Generation')
  print('-'*100)
  print('Rooms Occupied : ', room_id)
  check_out = date.today()
  book_id = record[0]  
  check_in = record[3]
  advance = record[5]
  total_days = (check_out - check_in).days
  result = room_exist(room_id)
  rent = result[3]
  amount = total_days * rent 
  gst_amount = amount * int(gst) /100
  st_amount = amount * int(st) /100
  payable_amount = amount - advance + gst_amount + st_amount
  print('Check In Date : ', check_in, '\n Check Out Date : ', check_out)
  print('Total Payable Days :', total_days)
  print('Room Rent Per Day :', rent)
  print('Total Amount : ', amount )
  print('Advance : ', advance, '\n GST ({}) : {}' .format(gst, gst_amount), '\n Service Tax ({}) : {}' .format(st, st_amount))
  print('Amount Payable : ', payable_amount)
  sql1 = 'update rooms set status = "free" where room_no =' +room_id+ ';'
  sql2 = 'update booking set check_out = "'+str(check_out)+'" where room_id = ' +room_id+ 'and cust_id = ' +cust_id+ ';'
  sql3 = 'insert into bill (book_id, amount, bill_date, gst, st) values ('+str(book_id)+', '+str(payable_amount)+', "'str(check_out)'", '+str(gst)+', '+str(st)+');'
  cursor.execute(sql1)
  cursor.execute(sql2)
  cursor.execute(sql3)
  conn.close()
  wait = input('\n\n\n Press Any Key To Continue..........')

def search_rooms():
  conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = 'Nagesh@38')
  cursor = conn.cursor()
  room_no = input('Enter Room No : ')
  sql = 'select * from rooms where room_no =' +room-no+ ';'
  cursor.execute(sql)
  record = cursor.fetchone()
  clear()
  print('Room Status')
  print('*'*120)
  print('Room No : ', record[1])
  print('Room Rent : ', record[2])
  print('Room Bed : ', record[3])
  print('Room Status : ', record[4])
  conn.close()
  wait = input('\n\n\n Press Any Key To Continue ...........')

def search_customer():
  conn = mysql.connctor.connect(host = 'localhost', database = 'hotel', user = 'root', password = 'Nagesh@38')
  cursor = conn.cursor()
  clear()
  print('Search Customer Database')
  print('*'*120)
  print('1.    Customer Name')
  print('2.    Customer Address')
  print('3.    Customer Phone')
  print('4.    Customer Email')
  print('5.    Id Proof')
  print('6.    Id Proof No')
  choice = int(input('Enter Your Choice : '))
  field_name = ''
  if choice == 1 :
    field_name = 'name'
  if choice == 2 :
    field_name = 'address'
  if choice == 3 :
    field_name = 'phone'
  if choice == 4 :
    field_name = 'email'
  if choice == 5 :
    field_name = 'id_proof'
  if choice == 6 :
    field_name = 'id_proof_no'
  value = input('Enter Value That You want To Search : ')
  if field_name == 'id' :
    sql = 'select * from customer where ' +field_name+ '=' +value+ ';'
  else :
    sql = 'select * from customer where ' +field_name+ 'like "%' +value+'%";'
  print(sql)
  cursor.execute(sql)
  records = cursor.fetchall()
  clear()
  print('Search Result For {} = {}'.format(field_name, value))
  print('*'*140)
  print('{} {:20s} {:30s} {:15s} {:30s} {:20s} {:15s}'.format('Id', 'Name', 'Address', 'Phone', 'Email', 'Id Used', 'Id No'))
  for record in records :
  print('{} {:20s} {:30s} {:15s} {:30s} {:20s} {:15s}'.format(record[0], record[1], record[2], record[3], record[4], record[5], record[6]))
  conn.close()
  wait = input('\n\n\n Press Any Key To Continue..........')

def search_booking():
  conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = 'Nagesh@38')
  cursor = conn.cursor()
  cust_no = input('Enter Customer No :')
  sql = 'select book_id, r.room_no, c.name, check_in, advance  from booking b, customer c, rooms r where b.room_id = r.id AND b.cust_id =' +cust_id+
  cursor.execute(sql)
  record = cursor.fetchall()
  clear()
  print('Booking Information For Customer Id : {}'.format(cust_no))
  print('{} {} {} {} {}'.format('Id', 'Room Id', 'Customer Name', 'Check In','Advance'))
  print('*'*140)
  for record in records:
    print('{} {} {} {} {}'.format(record[0], record[1], record[2], record[3], record[4]))
    conn.close()\
    wait = input('\n\n\n Press Any Key To Continue ............')

def search_bills():
  conn = mysql.connector.connect(host = 'localhost', database = 'hotel',  user = 'root', password = 'Nagesh@38')
  cursor = conn.cursor()
  bill_no = input('Enter Bill No : ')
  sql = 'select bill.bill_id, bill.amount, bill.date, gst, st, b.book_id, check_in, check_out, advance, name, address, phone, email, room_no \ from bill, booking b, customer c, rooms r \ where bill.book_id = b.book_id \ and b.room_id = r.id and b.cust_id = c.id AND NOT check_out is NULL AND \ bill_id = ' +bill_no+ ';'
  cursor.execute(sql)
  record = cursor.fetchone()
  clear()
  print('Bill Information For Bill No : {}'.format(bill_no))
  print('*'*140)
  print('Bill No', record[0])
  print('Amount', record[1])
  print('Bill Date', record[2])
  print('GST Charged', record[3])
  print('Service Tax Charged', record[4])
  print('Booking Id', record[5])
  print('Room Id', record[13])
  print('Check In Date', record[6])
  print('Check Out Date', record[7])
  print('Advance Paid', record[8])
  print('Customer Name', record[9])
  print('Customer Address', record[10])
  print('Customer Phone', record[11])
  print('Customer Email Id', record[12])
  conn.close()
  wait = input('\n\n\n Press Any Key To Continue.........')

def search_menu():
  while True:
    clear()
    print('Search Menu')
    print('*'*120)
    print("\n 1.    Room Status")
    print('\n 2.    Booking Status')
    print('\n 3.    Customer Details')
    print('\n 4.    Bills')
    print('\n 5.    Back To Main Menu')
    print('\n\n')
    choice = int(input('Enter Your Choice : '))
    if choice == 1 :
      search_rooms()
    if choice == 2 :
      search_booking()
    if choice == 3 :
      search_customer()
    if choice == 4 :
      search_bills()
    if choice == 5 :
      break

def report_room_status():
  conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = 'Nagesh@38')
  cursor = conn.cursor()
  sql = 'select * from rooms'
  cursor.execute(sql)
  records = cursor.fetchall()
  clear()
  print('Room Status - Report')
  print('- '*120)
  print('{:10s} {:10s} {:20s} {:20s} {:>40s} {:>30s} '.format('Room Id', 'Room No', 'Room Type', 'Rent', 'Bedding', 'Status'))
  for idr, no, rtype, rent, bed, status in records :
    print('{:<10d} {:<10d} {:20s} {:<7.2f} {:>40s} {:30s}'.format(idr, no, rtype, rent, bed, status))
  conn.close()
  wait = input('\n\n\n Press Any Key To Continue .......')

def report_booking_status():
  conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = 'Nagesh@38')
  cursor = conn.cursor()
  sql = 'select b.book_id, room_no, check_in, check_out, advance, name, address, phone \ where b.room_id = r.id and b.cust_id and check_out is NULL;'
  cursor.execute(sql)
  records = cursor.fetchall()
  clear()
  print('Booking Status - Report')
  print('-'*120)
  print('{:10s} {:10s} {:20s} {:20s} {:>30s} {:20s} {:30s} {:15s}'.format('Booking Id', 'Room No', 'Check In', 'Check Out', 'Advance', 'Name', 'Address', 'Phone'))
  for idr, no, check_in, check_out, advance, name, addr, phone in records:
    print('{:10d} {:10d} {:20s} {:20s} {:10.2f} {:20s} {:30s} {:15s}'.format(idr, no, str(check_in), str(check_out), advance, name, addr, phone))
  conn.close()
  wait = input('\n\n\n Press Any Key To Continue ........')

def report_menu():
    
  

    

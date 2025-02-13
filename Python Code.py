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
    global address
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
    elif record[1] == 'address':
        address = record[2]
    elif record[1] == 'phone':
        phone = record[2]
    elif record[1] == 'email':
        email = record[2]
    elif record[1] == 'gst':
        gst = record[2]
    elif record[1] == 'st':
        st = record[2]
    else:
        print("out of range")

def system_settings():
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
    elif choice == 2:
        field_name = 'address'
    elif choice == 3:
        field_name = 'phone'
    elif choice == 4:
        field_name = 'email'
    elif choice == 5:
        field_name = 'gst'
    elif choice == 6:
        field_name = 'st'
    else:
        print("out of range")

    value = input('Enter New value:')
    sql = "update setting set value =%s where field_name =%s ;"
    cursor.execute(sql)
    wait = input('\n\n\n Record updated ................ Press Any Key To Continue........')

def clear():
    for _ in range(65):
        print()

def room_exist(room_id,cursor):
    sql = "select * from rooms where room_no =%s ;"
    cursor.execute(sql,(room_id,))
    record = cursor.fetchone()
    return record

def get_room_details(room_id, cursor):
    sql = "select * from rooms where id = %s;"
    cursor.execute(sql,(room_id,))
    record = cursor.fetchone()
    return record

def customer_exist(cust_id,cursor):
    sql = "select * from customer where id =%s ;"
    cursor.execute(sql,(cust_id,))
    record = cursor.fetchone()
    return record

def add_room():
    clear()
    print('Add New Room - Screen')
    print('-'*120)
    room_no = input('\n Enter Room No : ')
    room_type = input('\n Enter Room Type (AC / DELUX / SUPER DELUX / QUEEN DELIGHT / KINGS SPECIAL / SUPER RICH  SPECIAL) : ')
    room_rent = input('\n Enter Room Rent (INR) : ')
    room_bed = input('\n Enter Room Bed Type  (SINGLE / DOUBLE / TRIPLE) : ')
    sql = "insert into rooms (room_no, room_type, room_rent, bed, status) values ( %s, %s, %s, %s, 'free';"
    result = room_exist(room_no)
    if result is None:
        cursor.execute(sql)
    else:
        print('\n\n\n Room No', room_no, 'Already Exist In Database')
    wait = input('\n\n\n Press Any Key To Continue..... ')

def modify_room():
    print('Change Room Information')
    print('*'*120)
    print('1.    Room Type')
    print('2.    Room Rent')
    print('3.    Room Bed')
    choice = int(input('Enter your choice : '))
    field_name = ''
    if choice == 1:
        field_name = 'room_type'
    elif choice == 2:
        field_name = 'room_rent'
    elif choice == 3:
        field_name = 'room_bed'
    else:
        print("out of range")
    room_no = input('Enter Room No : ')
    value = input('Enter New Value : ')
    sql = "update rooms set field_name = %s where room_no = %s ;"
    cursor.execute(sql)
    wait = input('\n\n\n Record Updated ................. Press Any Key To Continue......')

def add_customer():
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
    sql = "insert into customer(name, address, phone, email, id_proof, id_proof_no, males, females, children) values (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(sql,(name,address,phone,email,id_proof,id_proof_no,males,females,children))
    conn.commit()
    print('\n\n\n Customer Added Successfully .......... ')
    wait = input('\n\n\n Press Any Key To Continue ....... ')

def modify_customer():
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
    elif choice == 2:
        field_name = 'address'
    elif choice == 3:
        field_name = 'phone'
    elif choice == 4:
        field_name = 'email'
    elif choice == 5:
        field_name = 'id_proof'
    elif choice == 6:
        field_name == 'id_proof_no'
    elif choice == 7:
        field_name = 'males'
    elif choice == 8:
        field_name = 'females'
    elif choice == 9:
        field_name = 'children'
    else:
        print("out of range")
    cust_no = input('Enter Customer No : ')
    value = input('Enter New Value : ')
    sql = "update customer set field_name = %s where id =%s ;"
    cursor.execute(sql)
    wait = input('\n\n\n Record Updated ........... Press Any Key To Continue........')

def room_booking(conn, cursor):
    room_id = int(input('Enter Room No To Book: '))
    cust_id = int(input('Enter Customer Id: '))
    check_in = input('Enter Check In Date (YYYY-MM-DD): ')
    advance = float(input('Enter Advance Amount: '))
    sql1 = "UPDATE rooms SET status = 'occupied' WHERE id = %s;"
    sql2 = "INSERT INTO booking(room_id, cust_id, check_in, advance) VALUES (%s, %s, %s, %s);"
    if not room_exist(room_id, cursor):
        print(f"Room No {room_id} does not exist.")
    else:
        room_details = get_room_details(room_id, cursor)
        if room_details[5] == 'free' and customer_exist(cust_id, cursor):
            try:
                cursor.execute(sql1, (room_id,))
                cursor.execute(sql2, (room_id, cust_id, check_in, advance))
                conn.commit()
                print(f'\n\nRoom No {room_id} booked for Customer ID {cust_id} successfully!')
            except mysql.connector.Error as err:
                print(f"Error occurred: {err}")
                conn.rollback()  
        elif room_details[5] != 'free':
            print(f'\nRoom No {room_id} is not available for booking. Current status: {room_details[5]}')
        else:
            print('Customer does not exist. Please add the customer first in the database.')
    wait = input('\n\n\n Press Any Key To Continue..........')

def bill_generation():
    global gst
    global st
    room_id = input('Enter Room No : ')
    cust_id = input('Enter Customer Id : ')
    sql = "select * from booking where cust_id =%s and room_id =%s and check_out is NULL;"
    cursor.execute(sql,(cust_id,room_id))
    record = cursor.fetchone()
    if record is None:
        print('No active booking found for this room and customer.')
        return
    clear()
    print('Bill Generation')
    print('-'*100)
    print('Room Occupied : ', room_id)
    check_out = date.today()
    book_id = record[0]  
    check_in = record[3]
    advance = record[5]
    total_days = (check_out - check_in).days
    result = room_exist(room_id,cursor)
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
    bill_date = date.today()
    sql1 = "update rooms set status = 'free' where room_no =%s ;"
    sql2 = "update booking set check_out =%s where room_id =%s and cust_id =%s ;"
    sql3 = "insert into bill (book_id, amount, bill_date, gst, st) values (%s, %s, %s, %s, %s);"
    cursor.execute(sql1,(room_id,))
    cursor.execute(sql2,(check_out,room_id,cust_id))
    cursor.execute(sql3,(book_id,amount,bill_date,float(gst),float(st)))
    conn.commit()
    wait = input('\n\n\n Press Any Key To Continue..........')

def search_rooms():
    room_no = input('Enter Room No : ')
    sql = "select * from rooms where room_no =%s ;"
    cursor.execute(sql)
    record = cursor.fetchone()
    clear()
    print('Room Status')
    print('*'*120)
    print('Room No : ', record[1])
    print('Room Rent : ', record[2])
    print('Room Bed : ', record[3])
    print('Room Status : ', record[4])
    wait = input('\n\n\n Press Any Key To Continue ...........')

def search_customer():
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
    elif choice == 2 :
        field_name = 'address'
    elif choice == 3 :
        field_name = 'phone'
    elif choice == 4 :
        field_name = 'email'
    elif choice == 5 :
        field_name = 'id_proof'
    elif choice == 6 :
        field_name = 'id_proof_no'
    else:
        print("out of range")
    value = input('Enter Value That You want To Search : ')
    if field_name == 'id' :
        sql = "select * from customer where field_name =%s ;"
    else :
        sql = "select * from customer where field_name like %s ;"
    print(sql)
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Search Result For {} = {}'.format(field_name, value))
    print('*'*140)
    print('{} {:20s} {:30s} {:15s} {:30s} {:20s} {:15s}'.format('Id', 'Name', 'Address', 'Phone', 'Email', 'Id Used', 'Id No'))
    for record in records :
        print('{} {:20s} {:30s} {:15s} {:30s} {:20s} {:15s}'.format(record[0], record[1], record[2], record[3], record[4], record[5], record[6]))
    wait = input('\n\n\n Press Any Key To Continue..........')

def search_booking():
    cust_no = input('Enter Customer No :')
    sql = "select book_id, r.room_no, c.name, check_in, advance  from booking b, customer c, rooms r where b.room_id = r.id AND b.cust_id =%s ;"
    cursor.execute(sql)
    record = cursor.fetchall()
    clear()
    print('Booking Information For Customer Id : {}'.format(cust_no))
    print('{} {} {} {} {}'.format('Id', 'Room Id', 'Customer Name', 'Check In','Advance'))
    print('*'*140)
    for record in records:
        print('{} {} {} {} {}'.format(record[0], record[1], record[2], record[3], record[4]))
    wait = input('\n\n\n Press Any Key To Continue ............')

def search_bills():
    bill_no = input('Enter Bill No : ')
    sql = "select bill.bill_id, bill.amount, bill.date, gst, st, b.book_id, check_in, check_out, advance, name, address, phone, email, room_no \
           from bill, booking b, customer c, rooms r \
           where bill.book_id = b.book_id \
           and b.room_id = r.id and b.cust_id = c.id AND NOT check_out is NULL AND \
           bill_id =%s ;"
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
        elif choice == 2 :
            search_booking()
        elif choice == 3 :
            search_customer()
        elif choice == 4 :
            search_bills()
        elif choice == 5 :
            break
        else:
            print("out of range")
            
def report_room_status():
    sql = "select * from rooms"
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Room Status - Report')
    print('- '*120)
    print('{:10s} {:10s} {:20s} {:20s} {:>40s} {:>30s} '.format('Room Id', 'Room No', 'Room Type', 'Rent', 'Bedding', 'Status'))
    for idr, no, rtype, rent, bed, status in records :
        print('{:<10d} {:<10d} {:20s} {:<7.2f} {:>40s} {:30s}'.format(idr, no, rtype, rent, bed, status))
    wait = input('\n\n\n Press Any Key To Continue .......')

def report_booking_status():
    sql = "select b.book_id, room_no, check_in, check_out, advance, name, address, phone \
           where b.room_id = r.id and b.cust_id and check_out is NULL;"
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Booking Status - Report')
    print('-'*120)
    print('{:10s} {:10s} {:20s} {:20s} {:>30s} {:20s} {:30s} {:15s}'.format('Booking Id', 'Room No', 'Check In', 'Check Out', 'Advance', 'Name', 'Address', 'Phone'))
    for idr, no, check_in, check_out, advance, name, addr, phone in records:
        print('{:10d} {:10d} {:20s} {:20s} {:10.2f} {:20s} {:30s} {:15s}'.format(idr, no, str(check_in), str(check_out), advance, name, addr, phone))
    wait = input('\n\n\n Press Any Key To Continue ........')

def report_menu():
    while True :
        clear()
        print('Report Menu')
        print('\n 1.    Room Status')
        print('\n 2.    Booking Status')
        print('\n 3.    Today Collection')
        print('\n 4.    Monthly Collection')
        print('\n 5.    Back To Main Menu')
        print('\n\n')
        choice = int(input('Enter Your Choice : '))
        if choice == 1 :
            report_room_status()
        elif choice == 2 :
            report_booking_status()
        elif choice == 3 :
            report_today_collection()
        elif choice == 4 :
            report_monthly_collection()
        elif choice == 5 :
            break

def change_room_status():
    room_no = input('Enter Room No : ')
    status = input('Enter current Status (Renovation / Modification) : ')
    sql = "update rooms set status =%s where room_no =%s ;"
    cursor.execute(sql)
    print('\n\n Room Status Updated')
    wait = input('\n\n\n Press Any Key To Continue')

def main_menu():
    while True:
        clear()
        print('H O T E L     M A N A G E M E N T     S Y S T E M')
        print('*'*120)
        print('\n 1.    Add New Room')
        print('\n 2.    Add Customer')
        print('\n 3.    Modify Room Information')
        print('\n 4.    Modify Customer Information')
        print('\n 5.    Room Booking')
        print('\n 6.    Bill Generation')
        print('\n 7.    Search Database')
        print('\n 8.    Report Menu')
        print('\n 9.    Settings')
        print('\n10.    Close Application')
        print('\n\n')
        choice = int(input('Enter Your Choice : '))
        if choice == 1 :
            add_room()
        if choice == 2 :
            add_customer()
        if choice == 3 :
            modify_room()
        if choice == 4 :
            modify_customer()
        if choice == 5 :
            room_booking(conn,cursor)
        if choice == 6 :
            bill_generation()
        if choice == 7 :
            search_menu()
        if choice == 8 :
            report_menu()
        if choice == 9 :
            system_settings()
        if choice == 10 :
            break
      
if __name__ == "__main__" :
    settings()
    main_menu()

conn.close()

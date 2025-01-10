import mysql.connector
from datetime import date

# Global Variables
hotel_name = ''
address = ''
phone = ''
email = ''
gst = 0
st = 0
result = ''
result1 = ''

        
conn = mysql.connector.connect(host = 'localhost', database = 'hotel', user = 'root', password = 'Nagesh@38')
cursor = conn.cursor()


def room_exist(room_no):
    sql = "select * from rooms where room_no =%s ;"
    cursor.execute(sql)
    record = cursor.fetchone()
    return record

def customer_exist(cust_no):
    sql = "select * from customer where id =%s ;"
    cursor.execute(sql)
    record = cursor.fetchone()
    return record        


def room_booking():
    try:
        # Step 1: Take input from the user
        room_id = int(input('Enter Room No To Book : '))  # Room number to book
        cust_id = int(input('Enter Customer Id : '))  # Customer ID
        check_in = input('Enter Check In Date (YYYY-MM-DD) : ')  # Check-in date
        advance = float(input('Enter Advance Amount : '))  # Advance payment made by customer
        
        # Step 2: Check if the room exists and is available
        result = room_exist(room_id)  # Calls function to check room availability
        result1 = customer_exist(cust_id)  # Calls function to check if the customer exists

        # Step 3: Proceed if room is free and customer exists
        if result and result1:  # Ensure both room and customer data were returned
            if result[5] == 'free':  # Check if the room is free
                # SQL Query to update room status to 'occupied'
                sql1 = "UPDATE rooms SET status = 'occupied' WHERE id = %s;"
                cursor.execute(sql1, (room_id,))
                
                # SQL Query to insert booking details into booking table
                sql2 = "INSERT INTO booking(room_id, cust_id, check_in, advance) VALUES (%s, %s, %s, %s);"
                cursor.execute(sql2, (room_id, cust_id, check_in, advance))
                
                # Commit the transaction to save changes in the database
                conn.commit()
                print(f'\n\n\n Room No {room_id} booked for Customer ID {cust_id}')
            else:
                print(f'\n Room Is Not Available For Booking. Right Now It Is: {result[5]}')
        else:
            if result1 is None:
                print('Customer Does Not Exist ..... Please Add Customer First in Our Database')
            elif result is None:
                print('Room Does Not Exist.')
            else:
                print("Error: Unable to process the booking.")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Step 4: Wait for user action
    wait = input('\n\n\n Press Any Key To Continue.......')
room_booking()

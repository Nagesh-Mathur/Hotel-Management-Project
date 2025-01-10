import mysql.connector
from datetime import date

def room_booking(conn, cursor):
    room_id = int(input('Enter Room No To Book: '))
    cust_id = int(input('Enter Customer Id: '))
    check_in = input('Enter Check In Date (YYYY-MM-DD): ')
    advance = float(input('Enter Advance Amount: '))
    
    # SQL queries to update room status and insert booking details
    sql_update_room = "UPDATE rooms SET status = 'occupied' WHERE id = %s;"
    sql_insert_booking = "INSERT INTO booking(room_id, cust_id, check_in, advance) VALUES (%s, %s, %s, %s);"
    
    # Check if the room and customer exist
    if not room_exist(room_id, cursor):
        print(f"Room No {room_id} does not exist.")
    else:
        room_details = get_room_details(room_id, cursor)
        if room_details[5] == 'free' and customer_exist(cust_id, cursor):
            try:
                # Execute the queries to update room status and insert booking
                cursor.execute(sql_update_room, (room_id,))
                cursor.execute(sql_insert_booking, (room_id, cust_id, check_in, advance))
                
                # Commit the transaction
                conn.commit()
                print(f'\n\nRoom No {room_id} booked for Customer ID {cust_id} successfully!')
            except mysql.connector.Error as err:
                print(f"Error occurred: {err}")
                conn.rollback()  # Rollback if there is any error
        elif room_details[5] != 'free':
            print(f'\nRoom No {room_id} is not available for booking. Current status: {room_details[5]}')
        else:
            print('Customer does not exist. Please add the customer first in the database.')

    input('\n\nPress Any Key To Continue...')

# Define the room_exist function
def room_exist(room_id, cursor):
    cursor.execute("SELECT 1 FROM rooms WHERE id = %s;", (room_id,))
    return cursor.fetchone() is not None  # Return True if room exists, False otherwise

# Define the get_room_details function
def get_room_details(room_id, cursor):
    cursor.execute("SELECT * FROM rooms WHERE id = %s;", (room_id,))
    return cursor.fetchone()  # Return room details tuple

# Define the customer_exist function
def customer_exist(cust_id, cursor):
    cursor.execute("SELECT 1 FROM customer WHERE id = %s;", (cust_id,))
    return cursor.fetchone() is not None  # Return True if customer exists, False otherwise

# Main logic to establish connection
try:
    conn = mysql.connector.connect(
        host='localhost', 
        user='root', 
        password='Nagesh@38', 
        database='hotel'
    )
    cursor = conn.cursor()

    # Call the room_booking function with the connection and cursor
    room_booking(conn, cursor)
    
except mysql.connector.Error as err:
    print(f"Database connection error: {err}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()

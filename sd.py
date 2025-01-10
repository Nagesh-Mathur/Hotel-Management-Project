import mysql.connector

# Set up the connection to the database
conn = mysql.connector.connect(host='localhost', database='hotel', user='root', password='12345')
cursor = conn.cursor()

# Get user input for room details
'''room_no = input('Enter Room No: ')
room_type = input('Enter Room Type (e.g., AC, DELUX, etc.): ')
room_rent = float(input('Enter Room Rent: '))
room_bed = input('Enter Bed Type (e.g., SINGLE, DOUBLE, etc.): ')

# SQL query to insert a new room with 'free' status
sql = "INSERT INTO rooms (room_no, room_type, room_rent, room_bed, status) VALUES (%s, %s, %s, %s, 'free')"

try:
    # Execute the query
    cursor.execute(sql, (room_no, room_type, room_rent, room_bed))
    
    # Commit the changes to the database
    conn.commit()
    
    # Check if the insertion was successful
    if cursor.rowcount > 0:
        print("Room added successfully.")
    else:
        print("Failed to add room.")
except mysql.connector.Error as err:
    # Handle any errors that occur during execution
    print(f"Error: {err}")
    conn.rollback()  # Rollback if error occurs

# Close the connection'''




#def room_booking(conn, cursor):
room_id = int(input('Enter Room No To Book: '))
cust_id = int(input('Enter Customer Id: '))
check_in = input('Enter Check In Date (YYYY-MM-DD): ')
advance = float(input('Enter Advance Amount: '))
    
    # SQL queries to update room status and insert booking details
sql1 = "UPDATE rooms SET status = 'occupied' WHERE id = %s"
sql2 = "INSERT INTO booking(room_id, cust_id, check_in, advance) VALUES (%s, %s, %s, %s)"
print(sql1)
print(sql2)
    # Check if the room and customer exist
'''result = room_exist(room_id, cursor)  # Ensure this function returns the room details
    result1 = customer_exist(cust_id, cursor)  # Ensure this function returns customer details
    
    if result is None:
        print(f"Room No {room_id} does not exist.")
    elif result[5] == 'free' and result1 is not None:  # Assuming index 5 holds the status of the room
        try:
            # Execute the queries
            cursor.execute(sql1, (room_id,))
            cursor.execute(sql2, (room_id, cust_id, check_in, advance))
            
            # Commit the transaction
            conn.commit()
            print(f'\n\nRoom No {room_id} booked for Customer ID {cust_id} successfully!')
        except mysql.connector.Error as err:
            print(f"Error occurred: {err}")
            conn.rollback()  # Rollback if there is any error
    elif result[5] != 'free':
        print(f'\nRoom No {room_id} is not available for booking. Current status: {result[5]}')
    elif result1 is None:
        print('Customer does not exist. Please add the customer first in the database.')
    
    input('\n\nPress Any Key To Continue...')

# Define the room_exist and customer_exist functions
def room_exist(room_id, cursor):
    cursor.execute("SELECT * FROM rooms WHERE id = %s;", (room_id,))
    return cursor.fetchone()  # Assuming it returns a tuple with room details

def customer_exist(cust_id, cursor):
    cursor.execute("SELECT * FROM customers WHERE id = %s;", (cust_id,))
    return cursor.fetchone()  # Assuming it returns a tuple with customer details

# Main logic to establish connection
try:
    conn = mysql.connector.connect(
        host='localhost', 
        user='your_user', 
        password='your_password', 
        database='your_database'
    )
    cursor = conn.cursor()

    # Call the room_booking function with the connection and cursor
    room_booking(conn, cursor)
    
except mysql.connector.Error as err:
    print(f"Database connection error: {err}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()'''

import mysql.connector

# Establishing connection to the MySQL database 'debasis'
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',  # Replace with your actual password
    database='debasis'  # Connect to the 'debasis' database
)

# Creating a cursor object
mycursor = db.cursor()

# Step 1: Query data from the 'department' table
mycursor.execute("SELECT * FROM department")

# Step 2: Fetch all the rows from the result of the query
departments = mycursor.fetchall()

# Step 3: Display the fetched data
print("Data in 'department' table:")
for department in departments:
    print(department)

# Closing the cursor and the connection
mycursor.close()
db.close()

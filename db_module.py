import mysql.connector
# Initializes database 'mydata'
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database ="mydata"
)

cursor = mydb.cursor()

# creates the user table 
cursor.execute('''CREATE TABLE user(
    user_id INT PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    phone_num VARCHAR(15),
    email VARCHAR(30),
    occupant_num INT
)''')

# creates the timeslot table 
# timeslot is broken down into 2 hour frames for a single week 
# time is in 24 hour system and marks the start time 
# CONSTRAINT: all rooms have the same open/ close hour from 8-14 from Mon - Fri
cursor.execute('''CREATE TABLE timeslot(
    availability CHAR(1),
    time INT,
    day CHAR(3),
    room_num CHAR(5),
    PRIMARY KEY(time, day, room_num)
    FOREIGN KEY(room_num) REFERENCES room(room_num)
)''')

# creates the location table 
cursor.execute('''CREATE TABLE location(
    building VARCHAR(30) PRIMARY KEY
)''')

# creates the room table 
# CONSTRAINT: room number is unique 
cursor.execute('''CREATE TABLE room(
    room_num CHAR(5) PRIMARY KEY,
    availability CHAR(1),
    board_avail CHAR(1),
    building VARCHAR(10),
    timeslot INT,
    FOREIGN KEY(timeslot) REFERENCES timeslot(time),
    FOREIGN KEY(building) REFERENCES location(building)
)''')

#creates the booking table 
cursor.execute('''CREATE TABLE booking(
    booking_id INT PRIMARY KEY,
    user_num INT,
    time_slot INT,
    date DATE,
    FOREIGN KEY (user_num) REFERENCES user(user_id) ON DELETE CASCADE,
    FOREIGN KEY (time_slot) REFERENCES timeslot(time) ON DELETE CASCADE,
    FOREIGN KEY (date) REFERENCES timeslot(date) ON DELETE CASCADE
)''')

cursor.execute('''INSERT INTO location 
VALUES ("IK Learning Centre"), ("Library of Arts")
''')

cursor.execute('''INSERT INTO timeslot  
VALUES ('Y', 8, 'Mon', 'I2A'), ('Y', 10, 'Mon','I2A'), ('Y', 12, 'Mon','I2A'), 
        ('Y', 8, 'Mon', 'I2B'), ('Y', 10, 'Mon','I2B'), ('Y', 12, 'Mon','I2B'),
         ('Y', 8, 'Mon', 'L1C'), ('Y', 10, 'Mon','L1C'), ('Y', 12, 'Mon','L1C'), 
        ('Y', 8, 'Mon', 'L1D'), ('Y', 10, 'Mon','L1D'), ('Y', 12, 'Mon','L1D'),
        ('Y', 8, 'Tue', 'I2A'), ('Y', 10, 'Tue','I2A'), ('Y', 12, 'Tue','I2A'), 
        ('Y', 8, 'Tue', 'I2B'), ('Y', 10, 'Tue','I2B'), ('Y', 12, 'Tue','I2B'),
         ('Y', 8, 'Tue', 'L1C'), ('Y', 10, 'Tue','L1C'), ('Y', 12, 'Tue','L1C'), 
        ('Y', 8, 'Tue', 'L1D'), ('Y', 10, 'Tue','L1D'), ('Y', 12, 'Tue','L1D'),
        ('Y', 8, 'Wed', 'I2A'), ('Y', 10, 'Wed','I2A'), ('Y', 12, 'Wed','I2A'), 
        ('Y', 8, 'Wed', 'I2B'), ('Y', 10, 'Wed','I2B'), ('Y', 12, 'Wed','I2B'),
         ('Y', 8, 'Wed', 'L1C'), ('Y', 10, 'Wed','L1C'), ('Y', 12, 'Wed','L1C'), 
        ('Y', 8, 'Wed', 'L1D'), ('Y', 10, 'Wed','L1D'), ('Y', 12, 'Wed','L1D'),
        ('Y', 8, 'Thu', 'I2A'), ('Y', 10, 'Thu','I2A'), ('Y', 12, 'Thu','I2A'), 
        ('Y', 8, 'Thu', 'I2B'), ('Y', 10, 'Thu','I2B'), ('Y', 12, 'Thu','I2B'),
         ('Y', 8, 'Thu', 'L1C'), ('Y', 10, 'Thu','L1C'), ('Y', 12, 'Thu','L1C'), 
        ('Y', 8, 'Thu', 'L1D'), ('Y', 10, 'Thu','L1D'), ('Y', 12, 'Thu','L1D'),
        ('Y', 8, 'Fri', 'I2A'), ('Y', 10, 'Fri','I2A'), ('Y', 12, 'Fri','I2A'), 
        ('Y', 8, 'Fri', 'I2B'), ('Y', 10, 'Fri','I2B'), ('Y', 12, 'Fri','I2B'),
         ('Y', 8, 'Fri', 'L1C'), ('Y', 10, 'Fri','L1C'), ('Y', 12, 'Fri','L1C'), 
        ('Y', 8, 'Fri', 'L1D'), ('Y', 10, 'Fri','L1D'), ('Y', 12, 'Fri','L1D')
''')


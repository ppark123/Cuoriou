import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database ="mydata"
)

cursor = mydb.cursor()

cursor.execute('''CREATE TABLE user(
    user_id INT PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    phone_num VARCHAR(15),
    email VARCHAR(30),
    occupant_num INT
)''')

cursor.execute('''CREATE TABLE timeslot(
    availability CHAR(1),
    time INT,
    date DATE,
    PRIMARY KEY(time, date)
)''')

cursor.execute('''CREATE TABLE location(
    building VARCHAR(30) PRIMARY KEY
)''')

cursor.execute('''CREATE TABLE room(
    room_num INT PRIMARY KEY,
    availability CHAR(1),
    board_avail CHAR(1),
    building VARCHAR(10),
    timeslot INT,
    FOREIGN KEY(timeslot) REFERENCES timeslot(time),
    FOREIGN KEY(building) REFERENCES location(building)
)''')

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
VALUES ("IK Learning Centre"), ("Library of Arts"), ("WD Library")
''')

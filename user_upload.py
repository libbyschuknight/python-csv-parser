import csv
import sys
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS USER")

# Create table as per requirement
create_table = """CREATE TABLE USER (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(create_table)

name = 'Libby'
surname = 'Knight'
age = 40
sex = 'F'
year = 2000


# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO USER(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       (name, surname, age, sex, year)
# try:
   # Execute the SQL command
cursor.execute(sql)
   # Commit your changes in the database
db.commit()
# except:
   # Rollback in case there is any error
   # db.rollback()

# cursor.execute(sql)


# disconnect from server
db.close()




# --------------------------------------------------------
def validate_email_address(email):
    from email_validator import validate_email, EmailNotValidError


    try:
        v = validate_email(email_address, allow_smtputf8=False) # validate and get info
        email = v["email"] # replace with normalized form
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        sys.stdout.write(str(email + ' ' + str(e)) + '\n')


with open('users.csv', 'rb') as csvfile:
    users_reader = csv.DictReader(csvfile)
    for row in users_reader:

        name = row['name'].strip().title().replace('!', '')
        surname = row['surname'].strip().title().replace('!', '')
        email_address = row['email\t'].strip().lower()

        print name, surname, email_address

        validate_email_address(email_address)

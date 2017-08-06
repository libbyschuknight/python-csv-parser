import csv
import sys
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

# disconnect from server
db.close()



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

import csv
import sys
import MySQLdb

def validate_email_address(email):
    from email_validator import validate_email, EmailNotValidError
    try:
        v = validate_email(email, allow_smtputf8=False) # validate and get info
        email = v["email"] # replace with normalized form
        return True
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        sys.stdout.write(str(email + ' ' + str(e)) + '\n')
        return False


def format_name(name):
    ''' Strip whitepsace, make title case, replace any '!', and escape apostrophes'''
    return name.strip().title().replace('!', '').replace("'","''")

def format_email(email):
    '''Strip any whitepsace, make lowercase and escape aspostrophes'''
    return email.strip().lower().replace("'", "''")

def perform_database():
    '''Open db connection, drop table, create new table, open csv, parse csv data, validate emails, insert data into table, close db'''
    db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS USER")

    create_table = """CREATE TABLE USER (NAME  CHAR(20) NOT NULL, SURNAME  CHAR(20), EMAIL CHAR(20))"""
    cursor.execute(create_table)

    with open('users.csv', 'rb') as csvfile:
        users_reader = csv.DictReader(csvfile)
        for row in users_reader:
            name = format_name(row['name'])
            surname = format_name(row['surname'])
            email_address = format_email(row['email\t'])
            email_check = validate_email_address(email_address)

            if email_check == True:
                # Prepare SQL query to INSERT a record into the database.
                sql = "INSERT INTO USER(NAME, \
                SURNAME, EMAIL) \
                VALUES ('%s', '%s', '%s' )" % \
                (name, surname, email_address)
                try:
                    # Execute the SQL command
                    cursor.execute(sql)
                    # Commit your changes in the database
                    db.commit()
                except:
                    # Rollback in case there is any error
                    db.rollback()

                    # disconnect from server
                    db.close()



perform_database()

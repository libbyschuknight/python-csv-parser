

# import csv file
import csv

with open('users.csv', 'rb') as csvfile:
    users_reader = csv.DictReader(csvfile)
    for row in users_reader:
        name = row['name'].strip()
        surname = row['surname'].strip()
        email_address = row['email\t'].strip()
        print (name, surname, email_address)

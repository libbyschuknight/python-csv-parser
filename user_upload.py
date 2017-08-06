

# import csv file
import csv

with open('users.csv', 'rb') as csvfile:
    users_reader = csv.DictReader(csvfile)
    for row in users_reader:
        name = row['name'].strip().title().replace('!', '')
        surname = row['surname'].strip().title().replace('!', '')
        email_address = row['email\t'].strip().lower()
        print (name, surname, email_address)

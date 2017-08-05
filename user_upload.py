

# import csv file
import csv

with open('users.csv', 'rb') as csvfile:
    users_reader = csv.reader(csvfile, delimiter=',')
    for row in users_reader:
        print row

# Notes

## My plan

- import csv file into file

- format csv data into what is wanted for inserting into the database
  - ~~make name / surname capitalised~~
  - ~~emails to lowercase~~
  - ~~validate emails before inserting~~
    - ~~if invalid, do not insert, error message to STDOUT~~

- add database stuff to file & add csv file to db
  - ~~connect~~
  - ~~table~~
  - ~~insert~~
  - ~~execute~~
  - ~~commit~~
  - ~~close~~

- refactor code
  - tidy up
  - put into methods - made some small methods

- script command line directives
  - ~~--file[csv file name] – this is the name of the CSV to be parsed~~
  - --create_table – this will cause the MySQL users table to be built (and no further action on will be taken)
  - --dry_run – this will be used with the -- file directive in the instance that we want to run the script but not insert into the DB. All other functions will be executed, but the database won't be altered.
  - -u – MySQL username
  - -p – MySQL password
  - -h – MySQL host
  - --help – which will output the above list of directives with details.

- robust
- handles errors and exceptions gracefully

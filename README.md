# Python CSV Parser

My attempt at the Catalyst Python script task.

### Note:

I don't know much Python, I am a Ruby/Rails developer. 😜
I have worked hard on this and have decided to stop now (6pm Sunday night) at getting the first directive working (`--file`).
I am pretty pleased with what I have done considering I don't really now Python and have never written a python script like this. 😁

I don't know much about Ubuntu so not sure if it will run on that. Hope it does!

Sorry haven't used `apt-get or pear` for the libraries installed / imported.

It is using MySql 5.7.19.

Doh! Didn't take this in "(email should be set to a UNIQUE index)" until now, so sorry it is no a UNIQUE index (may change tomorrow evening).

Have only had time to get the first directive done.

### Using
Python 2.7.13

I have run using `python2`


### Libraries
For email validation have used the python-email-validator -  https://github.com/JoshData/python-email-validator.

Install with  `pip2 install email_validator`


### Database
Having major issues with this as in the past have played around with SilverStripe and Django stuff and think this is causing weird issues.

I have been trying to create a new database and then a new user but on doing `create user user_1; ` I have been getting this error:
`ERROR 1805 (HY000): Column count of mysql.user is wrong. Expected 45, found 48. The table is probably corrupted`

Google tells me that running `mysql_upgrade --force -uroot -p` should fix it by unfortunately it does not.

So, before I had this problem I was playing around following a tutorial and  will be using a database and user that works for me.

```
database = TESTDB
user = testuser
password = test123
```

### Install

To access, get into mysql with
```bash
mysql -u root -p
```

To set up database, user and grant permissions:

```sql
create database TESTDB;

show databases;

use TESTDB;

create user testuser;

grant all on TESTDB.* to 'testuser'@'localhost' identified by 'test123';
```

### To run script

`python user_upload.py --file users.csv`

My set up meant I was using `python2` instead of `python`.

### Commands

To see help:

`python user_upload.py --help`

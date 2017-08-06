# Python CSV Parser

My attempt at the Catalyst Python script task.

Note: I don't know much Python, I am a Ruby/Rails developer. 😜

Python 2.7.13

Run using `python2`


For email validation have used the python-email-validator

- https://github.com/JoshData/python-email-validator

- install with

  `pip2 install email_validator`


### Database
Having major issues with this as in the past have played around with SilverStripe and Django stuff and think this is causing me weird issues.

I have been trying to create a new database and then a new user but on doing `create user user_1; ` I have been getting this error:
`ERROR 1805 (HY000): Column count of mysql.user is wrong. Expected 45, found 48. The table is probably corrupted`

Google tells me that running `mysql_upgrade --force -uroot -p` should fix it by unfortunately it does not.

So, before I had this problem I was playing around following a tutorial and  will be using a database and user that works for me.

```
database = TESTDB
user = testuser
password = test123
```

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

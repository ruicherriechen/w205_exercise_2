Step-by-step Instruction:

Prerequisites:

1) PostgreSQL is properly installed
2) Python Version is 2.7
3) Storm is properly setup
4) Streamparse is setup (Virtualenv, Lein are installed)

To-do List:
1) Install Tweepy
	pip install tweedy
2) Install psycopg2
	pip install psycopg2
3) Create database on PostgreSQL
	- check PostgreSQL is up and running:
		ps auxwww | grep postgres
	- log into postgres as the postgres user:
		psql -U postgres
	- create database
		create database tcount;
	- change password for postgres user
		ALTER USER postgres WITH PASSWORD ‘password’;
4) Create table on PostgreSQL
	- run createtweetwordcounttable.py
		python createtweetwordcounttable.py
5) Run Tweetwordcount Project
	- cd /…/EXTweetwordcount (navigate to the directory)
	- sparse run
6) Show Final Result (under the folder where the .py file is stored)
	- python finalresults.py
	- python finalresults.py you
7) Run Histogram (under the folder where the .py file is stored)
	- python histogram.py 3 8 (note: no comma between two numbers)


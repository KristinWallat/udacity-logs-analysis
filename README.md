# udacity-logs-analysis
Project 1 for the udacity fullstack nanodegree

DESCRIPTION

For this assignment, I had to create a reporting tool that prints out reports in plain text based on a PostgreSQL database. Three questions had to be answered:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

REQUIREMENTS

* Python version 3.8.0
* Vagrant
* VirtualBox
* Git

SETUP

- Download and install Vagrant and VirtualBox.
- Download the VM configuration by forking and cloning the Github repository https://github.com/udacity/fullstack-nanodegree-vm.
- Change to the vagrant directory with cd /vagrant and start the virtual machine from the terminal inside the vagrant directory with vagrant up.
- When it is finished, use vagrant ssh to log into the virtual machine.
- Load the database with psql -d news -f newsdata.sql

RUNNING THE PROGRAM

- In order to answer the third question, I recommend creating VIEWS (see below)
- To run the reporting tool, use python logsanalysis.py

VIEWS

* In order to create VIEWS, type psql -d news
For anyone new to (SQL) programming, I recommend splitting the question in three parts to make it easier to understand what is happening. Experienced developers can join the three views in one view.

Part I - Get the top 3 error logs

news=>  CREATE VIEW error_logs AS SELECT count(*) AS stat, status, cast(time as date) AS day FROM log WHERE status='404 NOT FOUND' GROUP BY status, day ORDER BY stat desc limit 3;

***To see the result:***
 
news=> select * from error_logs;


Part II - Get the total visits with errortime

news=> CREATE VIEW total_visits AS SELECT count(*) as visitors, cast(time as date) AS errortime FROM log GROUP BY errortime;

Part III - Get the error days with visitors

news=> CREATE VIEW error_days AS SELECT * from error_logs join total_visits ON error_logs.day = total_visits.errortime;

***To see the result:***

news=> select * from error_days;







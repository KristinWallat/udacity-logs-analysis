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
- In order to answer the third question, I recommend creating VIEWS (see below)
- To run the reporting tool, use python logsanalysis.py

VIEWS

In order to create VIEWS, type psql -d news and run the following:

CREATE VIEW requests_errors AS
SELECT count(status) requests_errors , TO_CHAR(time, 'Month DD, YYYY') AS day FROM log WHERE status ='%404 NOT FOUND%' 
GROUP BY TO_CHAR(time, 'Month DD, YYYY') ORDER BY count(status) desc;

The Terminal should say "CREATE VIEW"
Exit "news" with \q



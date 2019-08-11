# udacity-logs-analysis
Project 1 for the udacity fullstack nanodegree

DESCRIPTION

For this assignment, I had to create a reporting tool that prints out reports in plain text based on an SQL database. Three questions had to be answered:
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
- To run the reporting tool, use python logsanalysis.py

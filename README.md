# logs-analysis-First-project
This is an internal reporting tool that produces answers by printing them out in the plain text in the Terminal. The tool produces answers to the following three questions based on the data in the database:

1) What are the most popular three articles of all time? 
2) Who are the most popular articles authors of all time? 
3) On which days did more than 1% of requests lead to errors? 

### Technologies That's used (Tools)
Writing the program with  tool is a [Python](https://www.python.org/downloads/release/python-361/) language program that uses the psycopg2 module to connect to the database. 

[Python](https://www.python.org/downloads/release/python-361/) For Writing program<br>
[PostgreSQL](https://www.postgresql.org/download/) Download For Database <br>
[VirtualBox](https://www.virtualbox.org/wiki/Downloads)<br>
[Vagrant](https://www.vagrantup.com/downloads.html)<br>
[Git](https://git-scm.com/downloads) <br>

VM configuration file by Udacity from [here](https://d17h27t6h515a5.cloudfront.net/topher/2017/May/59125904_fsnd-virtual-machine/fsnd-virtual-machine.zip) or clone the repository from [here] (https://github.com/udacity/fullstack-nanodegree-vm)<br>

Download Project Database from [newsdata](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
 
 # Editors
   can use any editor would do you like <br>
 [visual Studio Code](https://code.visualstudio.com/download)<br>
 [sublime Text](https://www.sublimetext.com/2)<br>
 [Atom](https://atom.io/)<br>
 [Brackets](http://brackets.io/)<br>
 
 

# Documentation <br>
Python : https://docs.python.org/3/tutorial/index.html<br>
Psycopg – PostgreSQL database adapter for Python : http://initd.org/psycopg/docs/index.html <br>
PostgreSQL: https://www.postgresql.org/docs/9.4/index.html<br>

## System setup and how to view this project
This project makes use of Udacity's Linux-based virtual machine (VM) configuration which includes all of the necessary software to run the application.
1. Download [Vagrant](https://www.vagrantup.com/) and install.
2. Download [Virtual Box](https://www.virtualbox.org/) and install. 
3. Clone this repository to a directory of your choice.
4. Download the **newsdata.sql** (extract from **newsdata.zip** (not provided here though)) and **newsdata.py** files from the respository and move them to your **vagrant** directory within your VM.

#### Run these commands from the terminal in the folder where your vagrant is installed in: 
1. ```vagrant up``` to start up the VM.
2. ```vagrant ssh``` to log into the VM.
3. ```cd /vagrant``` to change to your vagrant directory.
4. ```psql -d news -f newsdata.sql``` to load the data and create the tables.
5. ```python3 newsdata.py``` to run the reporting tool.


# Helpful Resources (README.md)
Python code quality
Your code should be written with good Python style. [The PEP8 style guide](https://www.python.org/dev/peps/pep-0008/) is an excellent standard to follow. You can do a quick check using the pep8 command-line tool.<br>
<br>
For more information on writing good READMEs, From udacity see this [course.](https://classroom.udacity.com/courses/ud777)

##  Troubleshooting
If your command prompt does not start with vagrant after typing `vagrant ssh` then please try the `winpty vagrant ssh` on your Windows system.

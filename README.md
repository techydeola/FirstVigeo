## FVS Web Loan Application


<p>The FVS web loan application is a web application for a company that allows the staff to easily make loan request and view thier loan history. This application is developed to simplify loan application and management for FirstVigeo Supermarket.

## Table of Content

- [About](#about)
- [Getting Started](#getting_started)
- [Installing](#installing)
- [Usage](#usage)
- [Collaboration](#collaboration)

## About
<p>This Application provides solution to FirstVigeo Supermarket Loan Application for Staffs and Loan Management by the Administration</p>

## Getting Started
1. Clone the repository using the command ```git clone https://github.com/techydeola/FirstVigeo```
2. To install django web framework, run ```pip3 install django``` if pip is already installed, otherwise run ```sudo apt install python3-pip```. Note: This command only works for Ubuntu users. If you use Windows or MacOS, search google on how to install these libraries.
3. To start the web server, navigate to the project root directory and run ```python3 manage.py runserver``` to start the development server.

## Installing
<p>This application runs on sqlite3 database, follow these instructions to get the database up and running</p>

1. In the project root directory create an empty file and name it ``db.sqlite3``
2. run ```python3 manage.py makemigrations```
3. run ```python3 manage.py migrate```

<p>Follow these steps to create an administrative user</p>

1. In the project root directory, run ```python3 manage.py createsuperuser```
2. Follow the prompts


## Usage
<p>Follow these steps for a quick example on how to use the web application (Admin Side)</p>

1. Start the development sever
2. Go to your browser (I recommend chrome), in the address bar enter ```localhost:8000\admin```
3. Login as an admin
4. Navigate to the staff menu and create a new staff, select only active for the staff permission (for regular staffs)


<p>Follow these steps for a quick example on how to use the web application (Client/Staff Side)</p>

1. Go to ```localhost:8000```
2. Click on Staff in the navigation bar
3. Login
4. Request for a new loan



### Collaboration
<p>This project was done and implemented by the following Software Enginners</p>

1. Johnson Adeola (johnsamxy@gmail.com)

<p align="center">ALX Portfolio Project</p>

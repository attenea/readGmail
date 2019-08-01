# readmyGmail
This program allows to automatically log in into Gmail, read the incomming emails and identify those who have the word "DevOps" (you can modify this word in the python file) in the body. It will also save those emails in a MySQL database. I'll be using MySQLClient database connector for Python, you can download it here: https://github.com/PyMySQL/mysqlclient-python. I also asume you have downloaded MySQL server.

# Getting Started
Please, follow the instructions below for downloading and running the program.

# Requisites
Make sure you have installed the following tools
```
Python 3.0 or later
```
Also, install all these Python packages
```bash
$ pip install MySQL-python
$ pip install mysqlclient
$ pip install google-api-python-client
$ pip install google-auth
$ pip install google-auth-oauthlib
$ pip install dateparser
$ pip install pybase64
$ pip install BeautifulSoup

```
# Instructions
readmyGmail works with the Gmail API so, before running the python file, you will need to have your own proyect associated with your gmail account. Follow the steps in this link: https://developers.google.com/gmail/api/quickstart/js. Once you have downloaded your own client_secret.json or client_id.json file, just add it in the same directory where the Python file (app.py) is. After running the program, the Gmail API will open a new window in your browser and ask for permission to log in. Then, you can run again the Python file and it will now read your incoming emails.

# Running
```
python app.py
```

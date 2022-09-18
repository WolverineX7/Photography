from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="shree7",
    database="photography",
    autocommit=True
)

cursor = mydb.cursor()


# Create your views here.
def home(requests):
    return render(requests, 'index.html')


def about(requests):
    return render(requests, 'about.html')


def login(requests):
    if requests.method == 'POST':
        username = requests.POST.get('username')
        password = requests.POST.get('password')
        cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s", (username, password,))
        account = cursor.fetchone()
        if account:
            return render(requests, 'index.html', {'message': 'Login successful'})
        else:
            return render(requests, 'login.html', {'message': 'Invalid username or password'})

    return render(requests, 'login.html')


def signup(requests):
    if requests.method == 'POST':
        username = requests.POST.get('username')
        email = requests.POST.get('email')
        password = requests.POST.get('password')
        password2 = requests.POST.get('password2')

        if password == password2: 
            cursor.execute("INSERT INTO user (username, email, password) VALUES (%s, %s, %s)", (username, email, password,))           
            return render(requests, 'login.html', {'message': 'User created successfully'})
        else:
            return render(requests, 'login.html', {'message': 'Password didn\'t match'})
    else:
        return render(requests, 'login.html')               


def portfolio(requests):
    return render(requests, 'portfolio.html')


def contact(requests):
    return render(requests, 'contact.html')


def index(requests):
    return render(requests, 'index.html')              
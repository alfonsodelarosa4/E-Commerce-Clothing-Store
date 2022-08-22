# E-Commerce-Clothing Store (Django/SQLite/Stripe)

## Overview
- This is an online store website. This application allows users to:
    - Create and sign in to their own accounts
    - View the store catalog
    - View product description of items
    - Add and remove items from cart
    - Process checkout with Stripe API

## Requirements
- On Visual Studio code, enter: ctrl + shift + P
    - Ensure that python.exe in the myEnv folder is selected
    - In other words, ensure that python runs on a virtual environment.

## Setup and Run
1. clone repository to your computer
```
git clone https://github.com/alfonsodelarosa4/E-Commerce-Clothing-Store.git
```
2. enter the following two commands:
    - Create migrations in the event that any models were changed:
```
python manage.py makemigrations
```
- Apply/Unapply migrations:
```
python manage.py migrate
```
3. run server
```
python manage.py runserver
```

## Features

### Create an account, log in, and log out
- Users can create an account with their email and password.
![](https://github.com/alfonsodelarosa4/blob/main/E-Commerce-Clothing-Store/demo_gifs/Django-Account.gif)

### Cart functionality: add items, remove items, change item count
- Users can add items, remove items, and change number of items in cart
![](https://github.com/alfonsodelarosa4/blob/main/E-Commerce-Clothing-Store/demo_gifs/Django-Cart.gif)

### Payment functionality
- Users can fill out two forms to pay for order (billing/shipping address and payment information)
![](https://github.com/alfonsodelarosa4/blob/main/E-Commerce-Clothing-Store/demo_gifs/Django-Payment.gif)

## Different Pages
- Store Catalog

- Log In Page

## SQLite Database Models
- User profile: user profile with email and password with Django's authentication
- Item: product items available for sale (with price, category, label, description)
- OrderItem: items in an order (with item, quantity)
- Order: an order made by a user (with user, start date, order date, shippping address, etc)
- Address: address (with street address, zip code, etc)
- Payment: payment made by user (stripe_charge id, amount)

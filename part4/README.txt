CS 334 – Part 4: Sweetleaf & Co. (Flask Backend)

Project Overview:
-----------------
This project implements the backend functionality for the Sweetleaf & Co. tea shop using Python Flask. The application allows customers to browse teas, add them to a cart, place an order, and receive a confirmation page. Admin users can view customer orders via an admin dashboard.

Files Included:
---------------
- flask_app.py              – Main Flask application with routes and database models
- /templates/               – HTML templates for all frontend pages (index, cart, checkout, admin, etc.)
- /static/                  – Static files including Bootstrap CSS, custom CSS, JS, and image assets
- Execution.pdf             – Screenshots showing the working application
- README.txt                – This file

Main Functionalities:
---------------------
- Homepage (`/`) lists four tea products with images and links to product pages
- Cart page (`/cart`) displays items added via localStorage and calculates total
- Checkout page (`/checkout2`) includes a form to submit orders
- Orders are saved to a SQLite database and redirected to `/order_confirmed`
- Admin dashboard (`/admin_index`) and order listing (`/admin_orders`) are accessible via Flask routes

Email Feature:
--------------
- Order confirmation email is configured via Flask-Mail using Brevo (Sendinblue)
- Due to PythonAnywhere's free-tier SMTP restrictions, live email sending is disabled in production
- The code for email generation and sending is implemented and tested

Running the Application:
------------------------
This project is deployed at:
https://zoemartinez1.pythonanywhere.com/

To run locally:
1. Install Flask and Flask-Mail:
   pip install flask flask_sqlalchemy flask_mail
2. Run the app:
   python flask_app.py

Credits:
--------
All development and testing was completed by Zoe Martinez.

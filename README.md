# Inventory Management System

## Overview
The Inventory Management System is a web application designed to streamline inventory tracking and management in makerspaces. Built with Django, it offers a user-friendly interface for real-time inventory monitoring, historical data analysis, and efficient resource management.

## Features
- **Real-Time Inventory Tracking**: Monitor and update inventory levels in real time.
- **Historical Data Analysis**: Access and analyze historical inventory records.
- **User Authentication**: Secure login with institutional credentials.
- **Interactive Data Visualizations**: Utilize Plotly for insightful inventory charts.

## Getting Started
### Prerequisites
- Python 3.x
- Django
- Other dependencies listed in `requirements.txt`

### Installation
1. Clone the repository: 
   ```
   git clone https://github.com/arturosalazar/inventory_management.git
   ```
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the Django migrations:
   ```
   python manage.py migrate
   ```
4. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage
After starting the server, navigate to `http://localhost:8000` in your web browser to access the Inventory Management System.

## Screenshots
### Home Page
![Home Page](https://github.com/arturosalazar/inventory_management/blob/main/images/screenshot-home-page.png)

### Home Page 2
![Home Page 2](https://github.com/arturosalazar/inventory_management/blob/main/images/screenshot-home-page2.png)

### Sign Up
![Sign Up](https://github.com/arturosalazar/inventory_management/blob/main/images/screenshot-signup.png)

### Log In
![Log In](https://github.com/arturosalazar/inventory_management/blob/main/images/screenshot-login.png)

### Dashboard (With Low Inventory)
![Dashboard With Low Inventory](https://github.com/arturosalazar/inventory_management/blob/main/images/screenshot-dashboard.png)

### Dashboard (No Low Inventory)
![Dashboard With No Low Inventory](https://github.com/arturosalazar/inventory_management/blob/main/images/screenshot-dashboard-full.png)

### Add Item
![Add Item](https://github.com/arturosalazar/inventory_management/blob/main/images/screenshot-add-item.png)

### Edit
![Edit](https://github.com/arturosalazar/inventory_management/blob/main/images/screenshot-edit.png)

### Delete
![Delete](https://github.com/arturosalazar/inventory_management/blob/main/images/screenshot-delete.png)

### Chart of Item
![Chart Item](https://github.com/arturosalazar/inventory_management/blob/main/images/screenshot-chart-item.png)

### Log Out
![Log Out](https://github.com/arturosalazar/inventory_management/blob/main/images/screenshot-logout.png)

# INTRODUCTION

This project is a prototype web application for "Rix Audio" an e-commerce store
that is an endpoint to browse and purchase audio accessories.

Rix Audio caters audio autput devices under three sub-brands namely:
 - RENO (Earphones)
 - RHEA (Headphones)
 - RESP (Portable Speakers)

The following are the contents of the prototype webapp:

    !Global
    - Navbar
    - - Brand Logo
    - - Navigation to Cart & Sub-Brand page
    - - Login Placeholder
    - Flash toast message
    - Footer

    Home Page
    - Carousel displaying trending products
    - Cards that link to sub-brand pages
    - List of product cards
    - About Brand Section
    - Feedback Section
    - Partner Exhibit Section
    - Subscription Section

    Sub-Brand Page
    - Header Carousel
    - RadioGroup to switch between sub-brands
    - Group of product cards of the sub-brand
    - Sub-brand cards

    Product Page
    - Header Carousel
    - About Section of Product
    - - Image Preview
    - - Product Details
    - - Feature List (unimplemented placeholder)
    - Price
    - Button to add product to cart
    - Button to route to Cart Page
    - Button to route to Sub-brand Page
    - - It routes to the sub-brand that the current product belongs to
    - Feedback Section
    - Browser More | Sub-brand cards

    Order Page | Cart
    - Product cards of items in Cart
    - - Button to remove product from cart
    - Total Price
    - Button to route to Sub-brand page
    - Button to remove all contents from cart
    - Button to proceed with cart to checkout

    Checkout Page
    - Personal Details from
    - Placeholder to proceed to payment gateway
    

# TECHNOLOGIES USED

  * [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
  * [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
  * [Flask](https://flask.palletsprojects.com/)
  * [Flask Bootstrap](https://pythonhosted.org/Flask-Bootstrap/)
  * [Flask SQLAlchemy](https://www.sqlalchemy.org/)
  * [Flask WTForms](https://wtforms.readthedocs.io/en/2.3.x/)
  * [email-validator](https://pypi.org/project/email-validator/)
  * [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

# HOW TO

## Automated Method
    - Run 'launch.ps1' or 'launch.sh' on Powershell from project root folder
    - Browse to http://localhost:5000/

## Manual Method
    - Set up & Activate venv Virtual Environment
    - Install Dependancies
    - - Flask
    - - flask_bootstrap
    - - flask_sqlalchemy
    - - flask_wtf
    - - email_validator
    - run the 'index.py' file from project root folder

# Image Placeholder Credits

    Courtesy of Photographers on Unsplash
    - https://unsplash.com/


# META

QUEENSLAND UNIVERSITY OF TECHNOLOGY
 School of Information Systems
 Faculty of Science and Engineering

IFN557 | Rapid Web Technology

Assessment 2
 - E-Commerce Store
  - Python Flask

Semester One, 2020

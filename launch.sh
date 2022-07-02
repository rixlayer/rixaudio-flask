#!/bin/bash
py -3 -m venv venv
venv\Scripts\activate
pip install Flask
pip install flask_bootstrap
pip install flask_sqlalchemy
pip install flask_wtf
pip install email_validator

py run.py
# Lab 5 – Guitar Database Querying with Python

## Introduction
This lab replicates Lab 4 SQL queries using Python and the MySQL connector. Unit tests are included to ensure each function works as expected.

## Description
Each function in `lab5.py` corresponds to one query from Lab 4 and connects to the `my_guitar_shop` MySQL database.

## Design
- MySQL database used for data retrieval
- Python's `mysql-connector-python` used for database interaction
- Unit tests written using `unittest` framework

## How to Run

1. Install dependencies:
   pip install mysql-connector-python

2. Edit the `get_connection()` function with your own MySQL password

3. Run queries manually:
   python lab5.py

4. Run unit tests:
   python test_lab5.py

## Files
- `lab5.py` - Contains the main query functions
- `test_lab5.py` - Unit tests for each query

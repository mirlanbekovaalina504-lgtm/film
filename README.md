# Online Cinema Ticket Booking System

This project is a course work developed as a web application for online cinema ticket booking.
The system allows users to view movies, check ratings and available sessions, select seats in the cinema hall,
and book tickets with QR-code based payment.

## Project Goal

The goal of this project is to develop a web-based information system that automates the process
of booking cinema tickets using modern web technologies.

## Main Features

- movie list browsing;
- movie rating display;
- cinema session selection;
- seat selection in the hall (available and occupied seats);
- booking timer;
- payment using QR code;
- administrative panel for managing movies and sessions.

## Project Architecture

The application is built using a client-server architecture based on the Django framework.
Data storage is implemented using an SQLite database.
The administrative interface is provided by Django Admin.

## Project Setup and Run

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

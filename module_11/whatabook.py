# Author: Gillenwater, Sam
# WhatABook Assignment

import sys
import mysql.connector
from mysql.connector import errorcode

# Database Configuration Attributes
DB_HOST = "127.0.0.1"
DB_USER = "whatabook_user"
DB_PASS = "MySQL8IsGreat!"
DB_NAME = "whatabook"


def get_integer_input(prompt):
    """Utility function to get integer input from user with error handling."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def register_user(cursor):
    """Function to register a new user."""
    email = input("Enter your email: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    try:
        cursor.execute("INSERT INTO User(email, first_name, last_name) VALUES (%s, %s, %s);",
                       (email, first_name, last_name))
        print("Registration successful!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print("Registration failed. Please try again.")


def show_books(cursor):
    """Function to display all books."""
    cursor.execute("SELECT * FROM Book;")
    books = cursor.fetchall()
    for book in books:
        print(book)


def show_locations(cursor):
    """Function to display all store locations and their hours."""
    cursor.execute("SELECT store_name, store_hours FROM Store;")
    stores = cursor.fetchall()
    for store in stores:
        print(f"Store: {store[0]}, Hours: {store[1]}")


def validate_user(cursor):
    """Function to validate the user's ID."""
    user_id = get_integer_input("Enter user_id: ")
    cursor.execute("SELECT * FROM User WHERE user_id = %s;", (user_id,))
    if cursor.fetchone():
        return user_id
    else:
        print("Invalid user_id!")
        return None


def show_account_menu():
    """Function to display the account menu."""
    print("1. Wishlist")
    print("2. Add Book")
    print("3. Main Menu")


def show_wishlist(cursor, user_id):
    """Function to display the user's wishlist."""
    cursor.execute("SELECT * FROM Wishlist WHERE user_id = %s;", (user_id,))
    wishlist = cursor.fetchall()
    for item in wishlist:
        print(item)


def show_books_to_add(cursor, user_id):
    """Function to display books available to add to the wishlist."""
    cursor.execute("""
    SELECT * FROM Book
    WHERE book_id NOT IN (SELECT book_id FROM Wishlist WHERE user_id = %s);
    """, (user_id,))
    books = cursor.fetchall()
    for book in books:
        print(book)


def add_book_to_wishlist(cursor, user_id):
    """Function to add a selected book to the user's wishlist."""
    book_id = get_integer_input("Select a book to add to your wishlist: ")
    cursor.execute("SELECT * FROM Book WHERE book_id = %s;", (book_id,))
    if not cursor.fetchone():
        print("Invalid book_id!")
        return

    cursor.execute("SELECT * FROM Wishlist WHERE user_id = %s AND book_id = %s;", (user_id, book_id))
    if cursor.fetchone():
        print("This book is already in your wishlist!")
    else:
        cursor.execute("INSERT INTO Wishlist(user_id, book_id) VALUES (%s, %s);", (user_id, book_id))
        print("Book added to wishlist!")


def main():
    """Main function to run the application."""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        sys.exit(1)

    cursor = connection.cursor()

    while True:
        print("0. Register")
        print("1. View Books")
        print("2. View Store Locations")
        print("3. My Account")
        print("4. Exit Program")

        choice = get_integer_input("Enter your choice: ")

        if choice == 0:
            register_user(cursor)
        elif choice == 1:
            show_books(cursor)
        elif choice == 2:
            show_locations(cursor)
        elif choice == 3:
            user_id = validate_user(cursor)
            if user_id:
                show_account_menu()
                account_choice = get_integer_input("Enter your choice: ")

                if account_choice == 1:
                    show_wishlist(cursor, user_id)
                elif account_choice == 2:
                    show_books_to_add(cursor, user_id)
                    add_book_to_wishlist(cursor, user_id)
                elif account_choice == 3:
                    continue
        elif choice == 4:
            print("Exiting the program...")
            break

    connection.close()


if __name__ == "__main__":
    main()

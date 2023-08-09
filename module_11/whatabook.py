# Author: Gillenwater, Sam
# WhatABook Assignment

import mysql.connector

# Database Configuration Attributes
DB_HOST = "localhost"
DB_USER = "your_username"
DB_PASS = "your_password"
DB_NAME = "whatabook"


# Function to register a new user
def register_user(cursor):
    # Get user details
    email = input("Enter your email: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    # Insert the new user into the User table
    cursor.execute("INSERT INTO User(email, first_name, last_name) VALUES (%s, %s, %s);",
                   (email, first_name, last_name))
    print("Registration successful!")


# Function to display all books
def show_books(cursor):
    cursor.execute("SELECT * FROM Book;")
    books = cursor.fetchall()
    for book in books:
        print(book)


# Function to display all store locations and their hours
def show_locations(cursor):
    cursor.execute("SELECT store_name, store_hours FROM Store;")
    stores = cursor.fetchall()
    for store in stores:
        print(f"Store: {store[0]}, Hours: {store[1]}")


# Function to validate the user's ID
def validate_user(cursor):
    user_id = input("Enter user_id: ")
    cursor.execute("SELECT * FROM User WHERE user_id = %s;", (user_id,))
    if cursor.fetchone():
        return user_id
    else:
        print("Invalid user_id!")
        return None


# Function to display the account menu
def show_account_menu():
    print("1. Wishlist")
    print("2. Add Book")
    print("3. Main Menu")


# Function to display the user's wishlist
def show_wishlist(cursor, user_id):
    cursor.execute("SELECT * FROM Wishlist WHERE user_id = %s;", (user_id,))
    wishlist = cursor.fetchall()
    for item in wishlist:
        print(item)


# Function to display books available to add to the wishlist
def show_books_to_add(cursor, user_id):
    cursor.execute("""
    SELECT * FROM Book
    WHERE book_id NOT IN (SELECT book_id FROM Wishlist WHERE user_id = %s);
    """, (user_id,))
    books = cursor.fetchall()
    for book in books:
        print(book)


# Function to add a selected book to the user's wishlist
def add_book_to_wishlist(cursor, user_id, book_id):
    cursor.execute("SELECT * FROM Wishlist WHERE user_id = %s AND book_id = %s;", (user_id, book_id))
    if cursor.fetchone():
        print("This book is already in your wishlist!")
    else:
        cursor.execute("INSERT INTO Wishlist(user_id, book_id) VALUES (%s, %s);", (user_id, book_id))
        print("Book added to wishlist!")


# Main function to run the application
def main():
    # Connect to the database
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )
    cursor = connection.cursor()

    # Main loop for user interaction
    while True:
        # Display the main menu
        print("0. Register")
        print("1. View Books")
        print("2. View Store Locations")
        print("3. My Account")
        print("4. Exit Program")

        choice = input("Enter your choice: ")

        # Handle user choices
        if choice == "0":
            register_user(cursor)
        elif choice == "1":
            show_books(cursor)
        elif choice == "2":
            show_locations(cursor)
        elif choice == "3":
            user_id = validate_user(cursor)
            if user_id:
                show_account_menu()
                account_choice = input("Enter your choice: ")

                if account_choice == "1":
                    show_wishlist(cursor, user_id)
                elif account_choice == "2":
                    show_books_to_add(cursor, user_id)
                    book_id = input("Select a book to add to your wishlist: ")
                    add_book_to_wishlist(cursor, user_id, book_id)
                elif account_choice == "3":
                    continue
        elif choice == "4":
            print("Exiting the program...")
            break

    # Close the database connection
    connection.close()


# Run the application
if __name__ == "__main__":
    main()

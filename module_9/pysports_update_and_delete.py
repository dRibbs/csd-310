# pysports_update_and_delete.py

# Author: Gillenwater, Sam
# Version: 1.0
# Description: This script will connect to the pysports database and will perform insert, update, and delete operations
# on the 'player' table. It will then display player records along with their team names before and after
# each operation to verify the changes.

# Note: Before running the script, ensure that you have installed the 'mysql-connector-python' package.

import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="booger",
            database="pysports"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def inner_join_query():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()

            # INNER JOIN query
            query = """
                SELECT p.player_id, p.first_name, p.last_name, t.team_name
                FROM player p
                INNER JOIN team t ON p.team_id = t.team_id
            """

            cursor.execute(query)
            result = cursor.fetchall()

            print("- - DISPLAYING PLAYERS - -")
            for player_id, first_name, last_name, team_name in result:
                print(f"Player ID: {player_id}")
                print(f"First Name: {first_name}")
                print(f"Last Name: {last_name}")
                print(f"Team Name: {team_name}\n")

            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
    else:
        print("Connection to the database failed.")

def insert_player_record():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()

            # Insert a new record into the player table
            query = """
                INSERT INTO player (first_name, last_name, team_id)
                VALUES ('Gollum', 'Ring Stealer', 1)
            """

            cursor.execute(query)
            connection.commit()
            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
    else:
        print("Connection to the database failed.")

def update_player_record():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()

            # Update the player's team to Team Sauron
            query = """
                UPDATE player SET team_id = 2 WHERE first_name = 'Gollum'
            """

            cursor.execute(query)
            connection.commit()
            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
    else:
        print("Connection to the database failed.")

def delete_player_record():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()

            # Delete the updated record (Gollum)
            query = """
                DELETE FROM player WHERE first_name = 'Gollum'
            """

            cursor.execute(query)
            connection.commit()
            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
    else:
        print("Connection to the database failed.")

if __name__ == "__main__":
    # Insert a new record
    insert_player_record()

    # Display players after the insert.
    inner_join_query()

    # Update the newly inserted record.
    update_player_record()

    # Display the players after update.
    inner_join_query()

    # Delete the updated record.
    delete_player_record()

    # Display the players after delete.
    inner_join_query()

    input("Press any key to continue...")

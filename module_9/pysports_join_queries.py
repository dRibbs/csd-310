# pysports_join_queries.py

# Author: Gillenwater, Sam
# Version: 1.0
# Description: This script connects to the pysports database and executes an INNER JOIN query
# between the player and team tables to display player records with their team names.

# Note: Before running the script, ensure that you have installed the 'mysql-connector-python' package.

import mysql.connector

# Function to connect to the database
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

# The function to execute the INNER JOIN query and display the results.
def inner_join_query():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()

            # INNER JOIN query..
            query = """
                SELECT p.player_id, p.first_name, p.last_name, t.team_name
                FROM player p
                INNER JOIN team t ON p.team_id = t.team_id
            """

            cursor.execute(query)
            result = cursor.fetchall()

            # Displyaing the records
            print("- - DISPLAYING PLAYER RECORDS - -")
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

# Entry point of the script
if __name__ == "__main__":
    inner_join_query()
    input("Press any key to continue...")

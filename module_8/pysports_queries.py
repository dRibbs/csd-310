import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "booger",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("Connected to MySQL database.")

    cursor = db.cursor()

    team_query = "SELECT team_id, team_name, mascot FROM team"
    cursor.execute(team_query)

    teams = cursor.fetchall()

    print("Teams:")
    for team in teams:
        print("Team Name: {}, Team ID: {}, Mascot: {}".format(team[1], team[0], team[2]))

    player_query = "SELECT player_id, first_name, last_name, team_id FROM player"
    cursor.execute(player_query)

    players = cursor.fetchall()

    print("\nPlayers:")
    for player in players:
        print("Player ID: {}, Name: {} {}, Team ID: {}".format(player[0], player[1], player[2], player[3]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid.")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist.")

    else:
        print(err)

finally:
    # Close the cursor and database connection
    cursor.close()
    db.close()
    print("\nConnection to MySQL database closed.")

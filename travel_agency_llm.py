import mysql
import mysql.connector
from llm import generate_sql

conn = mysql.connector.connect(
    host="localhost",
    user="root",                    # Connect to the database 
    password="",                    # Prompt the database connection
    database="travel_agency",
    port=3306
)

cursor = conn.cursor(dictionary=True)
print("\nWelcome to Krish's Travel Agency")  
print("\nWhat would you like to do?") # Give the user options for flight booking

while True:
    user_input = input(">> ")
    if user_input.lower() in ["exit", "quit"]:
        break
    try:
        sql = generate_sql(user_input)
        print("Ok. Will do")
        print("\nGenerated SQL:")   # Generate the data based on the request
        print(sql)

        cursor.execute(sql)

        if sql.lower().startswith("select"):
            results = cursor.fetchall()
            print("\nResult:")  # Fetch the data from the database and print it.
            for row in results:
                print(row)
        else:
            conn.commit()
            print("\nAction completed successfully.")

    except mysql.connector.Error as e:
        print("Database error:", e) # Unsucessful connection to database
    except Exception as e:
        print("LLM error:", e) # Error connecting to database

cursor.close() # Close the connection to the database
conn.close()  # Error being connected to the database

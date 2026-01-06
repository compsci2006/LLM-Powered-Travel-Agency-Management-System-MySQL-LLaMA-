import mysql
import mysql.connector
try:
    conn = mysql.connectcleor.connect(
        host="localhost",
        user="root",
        password="",
        database="travel_agency",
        port=3306
    )
    cursor = conn.cursor()
except mysql.connector.Error as e:
    print("Database connection failed:", e)
    exit()

role = input("Are you a passenger or agent? ").lower()

while True:
    try:
        choice = int(input(
            "\nWelcome to Krish's Travel Agency!\n"
            "1 = Book Flight (Passenger)\n"
            "2 = Cancel Flight (Agent)\n"
            "3 = Update Flight Destination (Agent)\n"
            "4 = Exit\n"
            "Enter your choice: "
        ))

        if role == "passenger" and choice == 1:
            firstname = input("Enter your first name: ")
            lastname = input("Enter your last name: ")
            age = int(input("Enter your age: "))
            flight_airline = input("Enter flight airline: ")
            flight_destination = input("Enter flight destination: ")

            insert_query = """
            INSERT INTO flight_agent
            (firstname, lastname, age, flight_airline, flight_destination)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(
                insert_query,
                (firstname, lastname, age, flight_airline, flight_destination)
            )
            conn.commit()

            print(f"\nThank you {firstname}, your flight to {flight_destination} is confirmed.")

        elif role == "agent" and choice == 2:
            lastname = input("Enter passenger last name to cancel flight: ")

            delete_query = "DELETE FROM flight_agent WHERE lastname = %s"
            cursor.execute(delete_query, (lastname,))
            conn.commit()

            if cursor.rowcount > 0:
                print("Flight successfully canceled.")
            else:
                print("No flight found for that passenger.")

        elif role == "agent" and choice == 3:
            lastname = input("Enter passenger last name: ")
            new_destination = input("Enter new destination: ")

            update_query = """
            UPDATE flight_agent
            SET flight_destination = %s
            WHERE lastname = %s
            """
            cursor.execute(update_query, (new_destination, lastname))
            conn.commit()

            if cursor.rowcount > 0:
                print("Flight destination updated successfully.")
            else:
                print("No matching passenger found.")

        elif choice == 4:
            print("\nThank you for using Krish's Travel Agency. Have a great day!")
            break
        else:
            print("Unauthorized action or invalid option.")

    except ValueError:
        print("Invalid input. Please enter a number.")
    except mysql.connector.Error as e:
        print("Database error:", e)

cursor.close()
conn.close()
print("Database connection closed.")

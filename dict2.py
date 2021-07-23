# Dictionary using mysql database
import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "adit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

query = cursor.execute("Select * FROM Dictionary WHERE Expression = 'ghost' ")
results = cursor.fetchall()

print(results)
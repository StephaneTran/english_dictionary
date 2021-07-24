# --------------------------------------------
# English dictionary using mysql database.
# Email stephanetran1@gmail.com
# --------------------------------------------
import mysql.connector
from difflib import get_close_matches

# Connect to mysql database containing a table with two fields: 
# Expression: word
# Definition: definition of word
con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

def get_def(word):
    """Retrieve the definition of word using sql queries."""
    query = cursor.execute(f"Select * FROM Dictionary WHERE Expression = '{word}'")
    results = cursor.fetchall()
    query2 = cursor.execute(f"Select * FROM Dictionary WHERE Expression LIKE '{word[0]}%{word[-1]}'")
    results2 = cursor.fetchall()
    alike_words = [tuple1[0] for tuple1 in results2]
    alike_def = [tuple1[1] for tuple1 in results2]
    x = get_close_matches(word, alike_words)
    if results: 
        for result in results:
            print(result[1])
    elif len(x) > 0:
        yn = input(f"Did you mean {x[0]} instead? Enter Y if yes, or N if no: ")
        if yn == "Y" or yn == "y":
            query3 = cursor.execute(f"Select * FROM Dictionary WHERE Expression = '{x[0]}'")
            results3 = cursor.fetchall()
            print(results3[0][1])
        elif yn == "N" or yn == "n":
            print("Word does not exist. Please re-enter a word.")
        else: 
            print("We do not understand your entry.")    
    else:
        print("Word does not exist.")

while True:
    word = input("Enter a word: ")
    if word == "\end":
        break
    else:
        get_def(word)
    continue



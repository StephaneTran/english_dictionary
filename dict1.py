# --------------------------------------------
# english dictionary using json data file
# email stephanetran1@gmail.com
# --------------------------------------------
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def get_def(word):
    """Retrieve the definition of word using json file."""
    word = word.lower()
    if word in data:
        return data[word]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input(f"Did you mean {get_close_matches(word, data.keys())[0]} instead? Enter Y if yes, or N if no: ")
        if yn == "Y" or yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "Word does not exist. Please re-enter a word."
        else: 
            return "We do not understand your entry."    
    else: 
        return "The word does not exist. Please re-enter a word."

while True:
    word = input("\n\end to exit.\nEnter a word: ")
    if word == "\end":
        break
    else:
        output = get_def(word)
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)
    continue

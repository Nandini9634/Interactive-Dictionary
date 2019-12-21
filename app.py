import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data :
        return data[w]
    elif w.capitalize() in data:
        return data[w.capitalize()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w , data.keys() , cutoff=0.8)) > 0:
        yn = input("Did you mean %s instead? If yes enter Y else N: " %get_close_matches(w , data.keys(), cutoff=0.8)[0] )
        
        if yn == "Y" or yn == "y":
            return data[get_close_matches(w , data.keys(), cutoff= 0.8)[0]]
        elif yn =="N" or yn == "n":
            return "The word Does not exist! Please check it again."
        else:
            return "We didn't understand your query."
    else :
        return "The word Does not exist! Please check it again."

str = input("Enter the word to be searched: ")

ans = translate(str)

if type(ans) == list:
    for data in ans:
        print(data)
else:
    print(ans)
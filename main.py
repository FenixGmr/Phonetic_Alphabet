import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:


data = pandas.read_csv("nato_phonetic_alphabet.csv")

a = {row.letter:row.code for (index, row) in data.iterrows()}

# gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

c = True
while c:
    word = input("Enter a word: ").upper()
    try:
        b = [a[name] for name in word]
        c = False
    except KeyError:
        print("Sorry only letters in the alphabet please.")
    else:
        print(b)




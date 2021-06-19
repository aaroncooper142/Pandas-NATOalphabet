
import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
#print(df)

#Loop through rows of a data frame
#for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

alpha_dict = {row.letter: row.code for (index, row) in df.iterrows()}
#alpha_dict = pd.Series(df.code.values,index=df.letter).to_dict()
#{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = input("Enter a word: ").upper()
    word_list = list(word)

    try:
        return_list = [alpha_dict.get(letter) for letter in word_list if letter in alpha_dict]
        # instead of alpha_dict.get(letter) could have used alpha_dict[letter]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")

        generate_phonetic()
    else:

        print(return_list)

generate_phonetic()

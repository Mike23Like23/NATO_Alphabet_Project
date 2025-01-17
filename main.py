student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

phonetic_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# for (index, row) in phonetic_data.iterrows():
#     print(index, row)
for row in phonetic_data.iterrows():
    code_dict = {row.letter:row.code for (index, row) in phonetic_data.iterrows()}
print(code_dict)

#TODO 1. Create a dictionary in this format:
# (code_dict = {})
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word:\t").upper()
message = [code_dict[letter] for letter in user_input]
print(message)
    # for char in user_input:
    #     if char == letter:
    #         print(1)


# code_list = []
# for (letter, code) in code_dict.items():
#     code_list.append(code)
#
# message = input("Enter a word:\t")
#
# for char in message:

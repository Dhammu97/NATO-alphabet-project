import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")
create_dict = {code.letter: code.code for (index, code) in file.iterrows()}
# print(create_dict)

word = input("Enter a word...? ").upper()
output_list = [create_dict[letter] for letter in word]
print(output_list)

# Write a program to print the words, characters, line in file

import os

fname = input("Enter the file name: ")

if os.path.isfile(fname):
    print(f"{fname} file exists")
    lin_count = word_count = char_count = 0
    with open(fname,'r') as file:
        for line in file:
            line+=1
            # We need to split the line to get the words
            words = line.split()
            word_count = word_count + len(words)
            char_count = char_count + len(line) # Here we need to take individual characters

        print("The number of lines: ", lin_count)
        print("The number of words: ",word_count)
        print("The number of Characters : ",char_count)

else:
    print(f"{fname} doesn't exist")
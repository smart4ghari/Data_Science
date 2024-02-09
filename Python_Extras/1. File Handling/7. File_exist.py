# Check file existance, if it's available print it's content
import os.path

file_name = input("Enter the file name: ")

if os.path.isfile(file_name):
    print(f"{file_name} file exists")
    print("It's content is: ")
    print("*" * 50)
    with open(file_name,'r') as file:
        text = file.read()
        print(text)

else:
    print(f"{file_name} file doesn't exist")
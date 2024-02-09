# Before and After modification of data

with open('Students.txt','r+') as file1:
    # Read the file
    text = file1.read()
    print("Data before Modification")
    print("*"*50)
    print(text)

    # Modify the file using seek() method
    file1.seek(17)
    file1.write("Creators you know!")

    # Again read from first index
    file1.seek(0)
    text = file1.read()
    print("Data after modification")
    print("*"*50)
    print(text)
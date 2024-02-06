# Using with statement

with open("generate_file.txt", "w") as file1:
    file1.write("Line 1\n")
    file1.write("Line 2\n")
    file1.write("Line 3\n")
    file1.write("Line 4\n")
    file1.write("Line 5\n")
    print("Is file closed? :", file1.closed)  # Still the file is open so we'll get False here

print("Is file closed? :", file1.closed)  # Here the file has been closed so we'll get True here

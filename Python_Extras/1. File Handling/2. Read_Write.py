"""1.Write Operation"""

# Step 1 : Open the file

File = open("New_file.txt",'w') # New_file.txt doesn't exist before\

# Step 2 : Do the operations

File.write("Hello, this is a new file generated due to write mode\n")
File.write("*--------------*")
File.write("No contents as of now!")
File.write("*--------------*")

# Note : File.writelines() is used to write multiple lines

print("Data written successfully for write!")
# Step 3 : Close the file

File.close()

"""2.Append Operation"""

# Step 1 : Again open the file for appending

File = open("New_file.txt","a")

# Step 2 : Do the operations

File.write("This is for appending\n")
File.write("We're using line breaks here\n")
File.write("This is the last line of the file")

# Step 3 : Close the file.

print("Data appended successfully")
File.close()
"""Create the file dynamically in a folder"""

# Step 1 : Getting the user input for creating a file
Name = input("Enter the file Name: ")
file1 = open(f"Check_folder\\{Name.lower()}.txt","w")

# Step 2 : Do the operations in the file

# Here I'm going to extract the user data by getting the response from the user itself
# Let's make it interactive

usr_name = input("Please enter your name: ")
usr_des = input("Please enter your designation (Working or Student) ")

if usr_des == "Working":
    usr_role = input("Please enter your role ")
    usr_cmp = input("Please enter your company name ")
    print("Thanks for entering your details ")

    # Writing once after getting the data
    file1.write(f"Hello! {usr_name} welcome to this file\n")
    file1.write(f"Really glad to know about you\n")
    file1.write(f"Now you're currently working as {usr_role} in {usr_cmp}")

elif usr_des == "Student":
    usr_role = input("Please enter your dept ")
    usr_col = input("Please enter your college name ")
    print("Thanks for entering your details ")

    # Writing once after getting the data
    file1.write(f"Hello! {usr_name} welcome to this file\n")
    file1.write(f"Really glad to know about you\n")
    file1.write(f"Now you're currently working as {usr_role} in {usr_col}")

else:
    print("Please enter your designation as 'Student' or 'Working' ")

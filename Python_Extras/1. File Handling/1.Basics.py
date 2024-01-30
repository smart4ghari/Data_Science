# To perform any operations on the file first we need to open the file.

# open()-> inbuilt function available in python
# Parameters : Name of the file, operation mode (purpose)


# Step1 : Open the file
f = open("sample_check.txt","r")

# Step2 : Do the operations

print(f"File name is : {f.name}")
print(f"File mode is : {f.mode}")
print(f"File is readable? {f.readable()}")
print(f"File is writable? {f.writable()}")
print(f"Is the file closed? - before closing: {f.closed}")

# Step3 : Close the file
f.close()
print(f"Is the file closed? - After closing: {f.closed}")

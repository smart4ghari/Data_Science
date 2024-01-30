# Step 1 : open the file


file1 = open(file='New_file.txt') # if we didn't specify anything means by default it's read mode

line = file1.readline()

while line != '':
    print(line,end='')
    line = file1.readline()
file1.close()
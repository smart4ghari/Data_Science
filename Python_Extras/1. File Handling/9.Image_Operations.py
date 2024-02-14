# Open the binary file in read mode

f1 = open("developer_1.png","rb")

# Open the binary file in write mode

f2 = open("new_image.png","wb")

data = f1.read() #Bytes
f2.write(data)
print("New image is available with the name: new_image.png")
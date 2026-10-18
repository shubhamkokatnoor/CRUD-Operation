# CRUD operation for read and create a new file.
file_name = input("enter a file name :")
file = open(file_name,'r')
data=file.read()
file.close()
file_name = input("enter a file name :")
file = open(file_name,'x')
file.write(data)
file.close()
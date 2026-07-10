# Program 1 – Create & Write File
'''
with open("notes.txt", "w") as file:
    file.write("Hello! Zumair welcome to file handling")
    file.close()
'''

'''
# Program 2 – Read File

file = open("notes.txt", "r")
# print(file.read()) # reads the file completely
print(file.read(6)) # only reads 6 characters of file
'''

# Program 3 – Append Data
'''
file = open("notes.txt", "a")
file.write("\nNeil") # jitni dafa run kry gy utni dafa add hoga
file.close()
'''
'''
# Program 4 – Read Line by Line
file = open("names.txt", "r")
print(file.readline()) # reads line by line
print(file.readline())
print(file.readline())
print(file.readline())
'''


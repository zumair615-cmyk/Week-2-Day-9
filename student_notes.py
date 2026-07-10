name = input("Enter Student Name: ")
course = input("Enter Course: ")
cgpa = input("Enter CGPA: ")

with open("students.txt", "a") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Course: {course}\n")
    file.write(f"CGPA: {cgpa}\n")
    file.write("----------------------\n")

print("Student Data Saved Successfully!")
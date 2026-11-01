# Login Security System
# Stored credentials
correct_username = "admin"
correct_password = "root"

# Input from user
username = input("Enter username: ")
password = input("Enter password: ")

# Conditions
if username == correct_username:
   if password == correct_password:
       print("Login Successful")
   else:
       print("Incorrect Password")
else:
   print("User not found")

file_name = "attendance.txt"

with open(file_name, "w") as file:
   file.write("Vaibhav - P - Admin - 01/11/2026 - 10:00 - 16:00\n")
   file.write("Rahul - P - Employee - 01/11/2026 - 10:00 - 16:00\n")

print("Initial attendance recorded.\n")

while True:
   print("\n1. Mark Attendance")
   print("2. View Attendance")
   print("3. Exit")
  
   choice = input("Enter your choice: ")
  
   if choice == "1":
       name = input("Enter employee name: ")
       status = input("Enter status (Present/Absent): ")
       department = input("Enter department: ")
       date = input("Enter date (DD/MM/YYYY): ")
       in_time = input("Enter in time (HH:MM): ")
       out_time = input("Enter out time (HH:MM): ")
      
       with open(file_name, "a") as file:
           file.write(f"{name} - {status} - {department} - {date} - {in_time} - {out_time}\n")
      
       print("Attendance marked successfully.")
  
   elif choice == "2":
       print("\n--- Attendance Records ---")
       try:
           with open(file_name, "r") as file:
               print(file.read())
       except FileNotFoundError:
           print("No attendance data found.")
  
   elif choice == "3":
       print("System Closed.")
       break
  
   else:
       print("Invalid choice! Try again.")
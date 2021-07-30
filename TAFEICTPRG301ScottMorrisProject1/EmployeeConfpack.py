# Program that receives  the contents of two packs, and applies those packs to a list of
# employees depending on their attendence at each day of the 2 day conference

# Import the date function from the datetime module
from datetime import date

# Store today's date for the report
dateToday = date.today()
currentDay = dateToday.day
currentMonth = dateToday.month
currentYear = dateToday.year
currentDate = str(currentDay) + "/" + str(currentMonth) + "/" + str(currentYear)

# Open the confpack file
confpackFile = open("confPack.txt", "r")

# Receive the data for both conference packages
normConfPack = confpackFile.readline().rstrip()
bonusConfPack = confpackFile.readline().rstrip()

# Open the employees file
employeesFile = open("employees.txt", "r")

# initialise the first employee
employeeData = employeesFile.readline()

# Loop through the employees until the end of the file is reached,
# applying the correct pack to each employee
while employeeData != "":
    splitData = employeeData.split(",")
    if len(splitData) == 2:
        print("\nReport Date: " + currentDate)
        print("Attendee: " + splitData[0] + ", " + splitData[1].rstrip() + " Pack/s: ")
    elif len(splitData) == 3:
        if splitData[2] == "Y":
            print("\nReport Date: " + currentDate)
            print("Attendee: " + splitData[0] + ", " + splitData[1] + " Pack/s: " + normConfPack)
        else:
            print("\nReport Date: " + currentDate)
            print("Attendee: " + splitData[0] + ", " + splitData[1] + " Pack/s: ")
    else:
        if splitData[2] == splitData[3] == "Y":
            print("\nReport Date: " + currentDate)
            print("Attendee: " + splitData[0] + ", " + splitData[1] + " Pack/s: " + normConfPack + ", " + bonusConfPack)
        elif splitData[2] == splitData[3] == "":
            print("\nReport Date: " + currentDate)
            print("Attendee: " + splitData[0] + ", " + splitData[1] + " Pack/s: ")
        else:
            print("\nReport Date: " + currentDate)
            print("Attendee: " + splitData[0] + ", " + splitData[1] + " Pack/s: " + normConfPack)
    employeeData = employeesFile.readline()

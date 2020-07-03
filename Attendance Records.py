# Name: Attendance Records
# Description: Recording attendance of students
# Author: Waleed Akhtar

import time
import reading_from_user
# Functions used:


def login():
    # Using a while loop for the login screen. If the entered username and password matches with what's on the file then
    # the user will be allowed to continue on
    while True:
        with open("login_details.txt") as login_user:
            username = login_user.readline().rstrip()
            password = login_user.readline().rstrip()

            print("Please enter your login details below")
            enter_username = reading_from_user.read_nonempty_alphabetical_string("Name: ")
            enter_password = reading_from_user.read_nonempty_string("Password: ")

            if enter_username == username and password == enter_password:
                print("Welcome", username)
                print("*" * 20)
                break
            else:
                print("Login failed. Username or Password incorrect. Please try again")


def modules():
    # Get the module name and code
    module_names = []
    module_codes = []
    with open("modules.txt", "r") as module:
        for lecture in module:
            module = lecture.rstrip().split(",")
            module[1] = module[1].strip()
            module_names.append(module[1])
            module_codes.append(module[0])
    return module_names, module_codes


def module_selection(module_names, module_codes):
    print(f"Please select a module:")
    for i, module in enumerate(module_names):
        print(f"{i+1}. {module_codes[i]}")
    selection = reading_from_user.read_range_integer("> ", min_range=1, max_range=2)
    selection = module_codes[selection - 1]
    return selection


def class_attendance(selection):
    # Using lists to get data from the files
    name = []
    present = []
    absent = []
    excused = []
    soft = open(f"{selection}.txt", "r")
    for attendance in soft:
        attendance = attendance.rstrip().split(",")
        name.append(attendance[0].strip())
        present.append(int(attendance[1].strip()))
        absent.append(int(attendance[2].strip()))
        excused.append(int(attendance[3].strip()))
    soft.close()
    return name, present, absent, excused


def modify_class_attendance(name, present, absent, excused):
    students = len(name)
    print(f"There are {students} students registered in this class")
    for i, students in enumerate(name):
        print(f"Student #{i + 1}: {name[i]}")
        print(f"1. Present \n2. Absent \n3. Excused")
        choice = reading_from_user.read_range_integer("> ", min_range=1, max_range=3)
        if choice == 1:
            present[i] = present[i] + 1

        elif choice == 2:
            absent[i] = absent[i] + 1

        elif choice == 3:
            excused[i] = excused[i] + 1

    return name, present, absent, excused


def update_attendance(name, present, absent, excused, selection):
    lecture = open(f"{selection}.txt", "w")
    for i, sudo in enumerate(name):
        lecture.write(sudo + "," + str(present[i]) + "," + str(absent[i]) + "," + str(excused[i]) + "\n")
    print(f"{selection}.txt has been updated with the new attendance figures")
    lecture.close()


def statistics(selection, name):
    # Lists used here to generate statistics
    names = []
    present = []
    absent = []
    excused = []
    students = len(name)
    print(f"Module selected: {selection}")
    print(f"Number of students: {students}")
    class_file = open(f"{selection}.txt", "r")
    for class_data in class_file:
        class_data = class_data.rstrip()
        line_info = class_data.split(",")
        names.append(line_info[0])
        present.append(int(line_info[1]))
        absent.append(int(line_info[2]))
        excused.append(int(line_info[3]))

    for i, lecture in enumerate(names):
        values = (lecture, present[i], absent[i], excused[i])

    total_class = present[i] + absent[i] + excused[i]
    print(f"Number of classes: {total_class}")

    present_list = sum(present)
    classes = sum(present + absent + excused)
    average_attendance = present_list/classes * 10
    print(f"Average Attendance: {average_attendance:.1f} days")

    lowest_attender = total_class * 70 / 100
    if total_class > lowest_attender:
        print(f"Low Attender(s): {names[i]}")
        low_attender = names[i]

    for i, name in enumerate(names):
        if present[i] == 0:
            print(f"Non Attender(s): {names[i]}")
        non_attender = names[i]

    highest_attender = max(present)
    for i, name in enumerate(names):
        if present[i] == highest_attender:
            print(f"Best Attender(s): {name}")
            print(f"Attended: {highest_attender}/{total_class}")
            highest_attender_name = name
    return students, total_class, average_attendance, low_attender, highest_attender_name, selection, non_attender


def file_stats(selection, students, total_class, average_attendance, low_attender, highest_attender_name,
               non_attender):
    # Getting the current time and saving it as a variable
    current_time = time.strftime("%H_%M_%S-%d-%m-%Y")
    if selection == "SOFT_6018":
        with open("SOFT_6018_stat_"+current_time.replace(" ", " ")+".txt", "w") as data_6018:
            data_6018.write(f"Module Code: {selection} \n")
            data_6018.write(f"Number of students: {students} \n")
            data_6018.write(f"Number of classes: {total_class} \n")
            data_6018.write(f"Average Attendance: {average_attendance:.1f} days \n")
            data_6018.write(f"Non-Attender(s): {non_attender} \n")
            data_6018.write(f"Lowest Attender(s): {low_attender} \n")
            data_6018.write(f"Highest Attender(s): {highest_attender_name} \n")
            data_6018.close()

    elif selection == "SOFT_6017":
        with open(f"SOFT_6017_stat_{current_time}.txt", "w") as data_6017:
            data_6017.write(f"Module Code: {selection} \n")
            data_6017.write(f"Number of students: {students} \n")
            data_6017.write(f"Number of classes: {total_class} \n")
            data_6017.write(f"Average Attendance: {average_attendance:.1f} days \n")
            data_6017.write(f"Non-Attender(s): {non_attender} \n")
            data_6017.write(f"Lowest Attender(s): {low_attender} \n")
            data_6017.write(f"Highest Attender(s): {highest_attender_name} \n")
            data_6017.close()


user = 1

print("Welcome to the CIT Attendance Record System")
print("=" * 50)


def main():
    login()
    # Main menu
    while user != 3:
        print("1: Record Attendance")
        print("2: Generate Statistics")
        print("3: Exit")

        choice = reading_from_user.read_range_integer("> ", min_range=1, max_range=3)
        if choice == 1:
            modules_name, modules_codes = modules()
            selection = module_selection(modules_name, modules_codes)
            name, present, absent, excused = class_attendance(selection)
            modify_class_attendance(name, present, absent, excused)
            update_attendance(name, present, absent, excused, selection)

        elif choice == 2:
            modules_name, modules_codes = modules()
            selection = module_selection(modules_name, modules_codes)
            name, present, absent, excused = class_attendance(selection)
            students, total_class, average_attendance, low_attender, highest_attender_name, selection, non_attender\
                = statistics(selection, name)
            file_stats(selection, students, total_class, average_attendance, low_attender, highest_attender_name
                       , non_attender)

        elif choice == 3:
            exit()


main()

# Student Data Management System using Python and SQLite3
# By Sajith Madhusankha
# Uses Colorama and prettytable Libraries

# Import sqlite3 Library
import sqlite3
# Import prettytable Library
from prettytable import PrettyTable
# Import colorama library
from colorama import init, Fore, Style


# Initialize colorama
init()


# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect('student.db')
cursor = conn.cursor()

# Defining create_table function to create the table
def create_table():
    """Create the students table if it doesn't exist"""
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            grade TEXT,
            address TEXT,
            contact TEXT,
            parent_name TEXT
        )
    ''')
    conn.commit()

# Definie add_student class. Asks for user input to get relevant data about student
def add_student():
    """Add a new student to the database"""
    name = input("Enter the student's name: ")
    age = int(input("Enter the student's age: "))
    grade = input("Enter the student's grade: ")
    address = input("Enter the student's address: ")
    contact = input("Enter the student's contact information: ")
    parent_name = input("Enter the student's parent name: ")

    # Insert the data into the table(students)
    cursor.execute('''
        INSERT INTO students (name, age, grade, address, contact, parent_name)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, age, grade, address, contact, parent_name))
    conn.commit()
    # Succesful message
    print(Fore.GREEN + "Student added successfully!" + Style.RESET_ALL)

# Define function to retrieve student data using their ID
def get_student_by_id():
    """Retrieve a student's information by ID"""
    student_id = int(input("Enter the student ID: "))
    cursor.execute('''
        SELECT * FROM students WHERE id=?
    ''', (student_id,))
    student = cursor.fetchone()
    # If student available print to screen
    if student:
        print_student_info(student)
    # If not print error message
    else:
        print(Fore.RED + "Student not found." + Style.RESET_ALL)

# Define function to retrieve student data using their grade
def get_student_by_grade():
    """Retrieve students by grade"""
    grade = input("Enter the grade: ")
    cursor.execute('''
        SELECT * FROM students WHERE grade=?
    ''', (grade,))
    students = cursor.fetchall()
    # If available print to screen
    if students:
        print_students_info(students)
    # If not show error message
    else:
        print(Fore.RED + "No students found." + Style.RESET_ALL)

# Define function to retrieve student data using their age
def get_student_by_age():
    """Retrieve students by age"""
    age = int(input("Enter the age: "))
    cursor.execute('''
        SELECT * FROM students WHERE age=?
    ''', (age,))
    students = cursor.fetchall()
    # If found print to screen
    if students:
        print_students_info(students)
    # If not show error message
    else:
        print(Fore.RED + "No students found." + Style.RESET_ALL)

# Define function to retrieve student data using their name
def get_student_by_name():
    """Retrieve students by name"""
    name = input("Enter the name: ")
    cursor.execute('''
        SELECT * FROM students WHERE name=?
    ''', (name,))
    students = cursor.fetchall()
    # If available print to screen
    if students:
        print_students_info(students)
    # If not show error message
    else:
        print(Fore.RED + "No students found." + Style.RESET_ALL)

# Define a function to update student data
def update_student():
    """Update a student's information by ID"""
    student_id = int(input("Enter the student ID: "))
    cursor.execute('SELECT * FROM students WHERE id=?', (student_id,))
    student = cursor.fetchone()
    if not student:
        print(Fore.RED + "Student not found." + Style.RESET_ALL)
        return

    print_student_info(student)

    print(f"\n{Fore.YELLOW}Update Student ID: {student[0]}{Style.RESET_ALL}")

    new_name = input("Enter the new name (leave blank to keep current name): ")
    new_name = new_name if new_name else student[1]

    new_age = input("Enter the new age (leave blank to keep current age): ")
    new_age = int(new_age) if new_age else student[2]

    new_grade = input("Enter the new grade (leave blank to keep current grade): ")
    new_grade = new_grade if new_grade else student[3]

    new_address = input("Enter the new address (leave blank to keep current address): ")
    new_address = new_address if new_address else student[4]

    new_contact = input("Enter the new contact information (leave blank to keep current contact information): ")
    new_contact = new_contact if new_contact else student[5]

    new_parent_name = input("Enter the new parent name (leave blank to keep current parent name): ")
    new_parent_name = new_parent_name if new_parent_name else student[6]

    update_query = 'UPDATE students SET name=?, age=?, grade=?, address=?, contact=?, parent_name=? WHERE id=?'
    cursor.execute(update_query, (new_name, new_age, new_grade, new_address, new_contact, new_parent_name, student_id))
    conn.commit()
    print(Fore.GREEN + "Student updated successfully!" + Style.RESET_ALL)

# Define a function to delete student from the table
def delete_student():
    """Delete a student's information by ID"""
    student_id = int(input("Enter the student ID: "))
    cursor.execute('SELECT * FROM students WHERE id=?', (student_id,))
    student = cursor.fetchone()
    if not student:
        print(Fore.RED + "Student not found." + Style.RESET_ALL)
        return

    print_student_info(student)

    confirmation = input(f"Are you sure you want to delete {student[1]} (Y/N)? ")
    if confirmation.lower() == 'y':
        cursor.execute('DELETE FROM students WHERE id=?', (student_id,))
        conn.commit()
        print(Fore.GREEN + "Student deleted successfully!" + Style.RESET_ALL)

# Define a function to get all student details in a table
def list_students():
    """Retrieve a list of all students"""
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    if students:
        print_students_info(students)
    else:
        print(Fore.YELLOW + "No students found." + Style.RESET_ALL)


def close_connection():
    """Close the database connection"""
    cursor.close()
    conn.close()

# Main menu Interface
def display_main_menu():
    """Display the main menu options"""
    menu = f'''
{Fore.MAGENTA}╔════════════════════════════════════════════════════════╗
║             Student Data Management System             ║
╠════════════════════════════════════════════════════════╣
║   {Fore.YELLOW}1. Add Student{Fore.MAGENTA}                                       ║
║   {Fore.YELLOW}2. Get Student{Fore.MAGENTA}                                       ║
║   {Fore.YELLOW}3. Update Student{Fore.MAGENTA}                                    ║
║   {Fore.YELLOW}4. Delete Student{Fore.MAGENTA}                                    ║
║   {Fore.YELLOW}5. List Students{Fore.MAGENTA}                                     ║
║   {Fore.YELLOW}6. Quit{Fore.MAGENTA}                                              ║
╚════════════════════════════════════════════════════════╝{Style.RESET_ALL}

Enter the number of your choice (1-6):
'''
    print(menu)

# Get student menu interface
def display_get_student_menu():
    """Display the "Get Student" menu options"""
    menu = f'''
{Fore.MAGENTA}╔════════════════════════════════════════════════════════╗
║                    Get Student Menu                    ║
╠════════════════════════════════════════════════════════╣
║   {Fore.YELLOW}1. Get Student by ID{Fore.MAGENTA}                                 ║
║   {Fore.YELLOW}2. Get Student by Grade{Fore.MAGENTA}                              ║
║   {Fore.YELLOW}3. Get Student by Age{Fore.MAGENTA}                                ║
║   {Fore.YELLOW}4. Get Student by Name{Fore.MAGENTA}                               ║
║   {Fore.YELLOW}5. Return to Main Menu{Fore.MAGENTA}                               ║
╚════════════════════════════════════════════════════════╝{Style.RESET_ALL}

Enter the number of your choice (1-5):
'''
    print(menu)

# Define function to print details to the screen(single student)
def print_student_info(student):
    """Print a student's information"""
    table = PrettyTable()
    table.field_names = ["ID", "Name", "Age", "Grade", "Address", "Contact", "Parent Name"]
    table.add_row(student)
    print(Fore.CYAN + table.get_string() + Style.RESET_ALL)

# Define function to print details to the screen(Multiple students)
def print_students_info(students):
    """Print students' information"""
    table = PrettyTable()
    table.field_names = ["ID", "Name", "Age", "Grade", "Address", "Contact", "Parent Name"]
    for student in students:
        table.add_row(student)
        table.add_row(["------", "------", "------", "------", "------", "------", "------"])
    print(Fore.CYAN + table.get_string() + Style.RESET_ALL)

# Define main
def main():
    create_table()
    while True:
        display_main_menu()
        main_choice = input()
        if main_choice == '1':
            add_student()
        elif main_choice == '2':
            while True:
                display_get_student_menu()
                get_student_choice = input()
                if get_student_choice == '1':
                    get_student_by_id()
                elif get_student_choice == '2':
                    get_student_by_grade()
                elif get_student_choice == '3':
                    get_student_by_age()
                elif get_student_choice == '4':
                    get_student_by_name()
                elif get_student_choice == '5':
                    break
                else:
                    print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
        elif main_choice == '3':
            update_student()
        elif main_choice == '4':
            delete_student()
        elif main_choice == '5':
            list_students()
        elif main_choice == '6':
            close_connection()
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)


# Run the program
main()

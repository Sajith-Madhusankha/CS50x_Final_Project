# Simple Student Data Management System
#### Video Demo: <https://youtu.be/uN9-pWp9xyo>
#### Description: This Program Helps to manage student data using Python and SQLite. User can
 - add student to the table
 - Search for student/s using
    - ID
    - Name
    - Age
    - Grade
- Update Student Details
    - Leave blanks if no need to change particular details
- Delete students from the table
    - Asks for confirmation showing the student details
- List all the student available in the table
- Exit

I Used Few Libraries in this project
 1. SQLite
    - install using
    ```
      pip install sqlite
    ```
2. prettytable
    - install using
    ```
    pip install prettytable
    ```
3. Colorama
    - install using
    ```
    pip install colorama
    ```

Here's preview of the code.
 - create_table function used to create a table if not already available. I used ID as primary key. I Didnt used autoinrement because it will change all student ID's when i delete a student in middle of the table. I used the following data types for each column
    - name TEXT
    - age INTEGER
    - grade TEXT
    - address TEXT
    - contact TEXT
    - parent_name TEXT

 - add_student function asks for user input to get student name, age, grade, address, contact info and parent name. After entering all data successful meassage will be printed to screen. and the data will be added to student database. If few fields left empty program will show error message.

 - There are seperate functions to search student. get_student_by_id search students by Id and print if search ID is available. If not available it'll print Student not found message. all other search functions works this way.
    - get_student_by_age
    - get_student_by_grade
    - get_student_by_name

- update_student function used to update student details. it'll ask for new values for each criteria. if user leaves an empty field old value will remain intact.

- delete_student function search student by ID and if available prompt the user asking to confirm the deletion.

- list_students retrieve all the student data in a table

- prettytable and colorama libraries used to make user interface more beautiful. Also it helps to read the data in a output table easily.

- main function can be explained as following,
  - The code begins with a definition of the main function, which serves as the entry point for the program. The main function is responsible for coordinating various operations and presenting a menu-driven interface to the user.
  - The first action in the main function is to create a table.
  - After creating the table, the program enters an infinite loop, indicating that it will continue running until explicitly terminated. Within this loop, the main menu is displayed to the user, presenting various options to choose from. The user's choice is obtained through the input() function and stored in the variable main_choice.
  - If the user selects option 1, the program calls the add_student() function.
  - If the user selects option 2, another nested loop is initiated to handle the various ways to retrieve student information. The get_student_menu() function is displayed, presenting a submenu of options related to retrieving student records. The user's choice is stored in the variable get_student_choice.
  - If the user selects option 3, the update_student() function is called. This function allows the user to modify the information of an existing student. It prompts the user to enter a student ID, retrieves the corresponding record, and provides options to update specific fields such as name, grade, or age.
  - If the user selects option 4, the delete_student() function is called. This function prompts the user to enter a student ID and removes the corresponding student record from the table.
  - If the user selects option 5, the list_students() function is called. This function retrieves and displays all the student records in the table, providing an overview of the current student population.
  - If the user selects option 6, the program calls the close_connection() function, which presumably handles any necessary cleanup tasks and closes the connection to the database. This action signifies the end of the program, and the main loop is terminated by breaking out of it.
  - If the user enters an invalid choice at any point, an error message is displayed in red text, indicating that the selection was not recognized. This helps guide the user to choose a valid option from the menu.
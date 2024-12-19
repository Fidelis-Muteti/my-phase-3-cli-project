# CLI Project
# Employee Management System

## Project Overview
The Employee Management System is a simple application designed to manage supervisors, employees, and their assigned duties. It provides a CLI-based interface to perform CRUD operations on supervisors, employees, and duties while maintaining their relationships.

## Features

### Supervisor Management
- **Create Supervisor**: Add a new supervisor with a name and email.
- **Update Supervisor**: Edit the details of an existing supervisor.
- **Delete Supervisor**: Remove a supervisor from the database.
- **List Supervisors**: View all supervisors in the system.

### Employee Management
- **Create Employee**: Add a new employee with a name, age, and assign them to a supervisor.
- **Update Employee**: Modify the details of an existing employee, including changing their assigned supervisor.
- **Delete Employee**: Remove an employee from the database.
- **View Employees by Supervisor**: List all employees working under a specific supervisor.



## Project Structure
```
project/
|-- models.py          # Contains database models for Supervisor, Employee, and Duty
|-- cli.py             # CLI-based interface for managing the system
|-- requirements.txt   # Python dependencies (if applicable)
|-- supervisors.db             # SQLite database file (auto-generated)
```

## Database Schema
1. **Supervisor**:
   - `id`: Integer (Primary Key)
   - `name`: String (Supervisor's name)
   - `email`: String (Unique email address)

2. **Employee**:
   - `id`: Integer (Primary Key)
   - `name`: String (Employee's name)
   - `age`: Integer (Employee's age)
   - `supervisor_id`: Integer (Foreign Key to Supervisor)

3. **Duty**:
   - `id`: Integer (Primary Key)
   - `description`: String (Duty description)
   - `employee_id`: Integer (Foreign Key to Employee)

## Installation

### Prerequisites
- Python 3.x
- SQLite

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/employee-management-system.git
   cd employee-management-system
   ```

2. Install dependencies (if using a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize the database:
   ```bash
   python cli.py
   ```
   The database will be created automatically.

## Usage
Run the application by executing:
```bash
python cli.py
```
Follow the on-screen instructions to perform various operations, such as creating supervisors, employees, and duties.

## Example
- **Create a Supervisor**:
  ```
  Enter TM name: John Doe
  Enter TM email: john.doe@example.com
  TM 'John Doe' created with ID 1
  ```

- **Assign an Employee to a Supervisor**:
  ```
  Enter Employee name: Jane Smith
  Enter Employee age: 30
  Enter Supervisor ID: 1
  Employee 'Jane Smith' created with ID 1 and assigned to Supervisor ID 1
  ```



## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## Contact
For questions or suggestions, contact:
- **Name**: Fideis Muteti
- **Email**:fidelmwovi@gmail.com

---
Thank you for using the Employee Management System!


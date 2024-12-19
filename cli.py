import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Supervisor, Employee

DATABASE_URL = "sqlite:///supervisors.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    # Initialize Database
    Base.metadata.create_all(engine)
    print("Database Initialized")

def create_supervisor():
    name = input("Enter Supervisor name: ")
    email = input("Enter Supervisor email: ")
    supervisor = Supervisor(name=name, email=email)
    session.add(supervisor)
    session.commit()
    print(f"Supervisor '{name}' created with ID {supervisor.id}")

def update_supervisor():
    supervisor_id = int(input("Enter Supervisor ID to update: "))
    supervisor = session.get(Supervisor, supervisor_id)
    if not supervisor:
        print(f"Supervisor with ID {supervisor_id} does not exist.")
        return
    supervisor.name = input(f"Enter new name for Supervisor (current: {supervisor.name}): ") or supervisor.name
    supervisor.email = input(f"Enter new email for Supervisor (current: {supervisor.email}): ") or supervisor.email
    session.commit()
    print(f"Supervisor ID {supervisor_id} updated successfully")

def delete_supervisor():
    supervisor_id = int(input("Enter Supervisor ID to delete: "))
    supervisor = session.get(Supervisor, supervisor_id)
    if not supervisor:
        print(f"Supervisor with ID {supervisor_id} does not exist.")
        return
    session.delete(supervisor)
    session.commit()
    print(f"Supervisor ID {supervisor_id} deleted successfully.")

def create_employee():
    name = input("Enter Employee name: ")
    age = int(input("Enter Employee age: "))
    supervisor_id = int(input("Enter Supervisor ID: "))
    supervisor = session.get(Supervisor, supervisor_id)
    if not supervisor:
        print(f"Supervisor with ID {supervisor_id} does not exist.")
        return
    employee = Employee(name=name, age=age, supervisor_id=supervisor_id)
    session.add(employee)
    session.commit()
    print(f"Employee '{name}' created with ID {employee.id} and assigned to Supervisor ID {supervisor_id}")

def update_employee():
    employee_id = int(input("Enter Employee ID to update: "))
    employee = session.get(Employee, employee_id)
    if not employee:
        print(f"Employee with ID {employee_id} does not exist.")
        return
    employee.name = input(f"Enter new name for Employee (current: {employee.name}): ") or employee.name
    employee.age = int(input(f"Enter new age for Employee (current: {employee.age}): ") or employee.age)
    new_supervisor_id = input(f"Enter new Supervisor ID for Employee (current: {employee.supervisor_id}): ") or employee.supervisor_id
    if new_supervisor_id:
        new_supervisor = session.get(Supervisor, int(new_supervisor_id))
        if not new_supervisor:
            print(f"Supervisor with ID {new_supervisor_id} does not exist. Skipping Supervisor update.")
        else:
            employee.supervisor_id = new_supervisor_id
    session.commit()
    print(f"Employee ID {employee_id} updated successfully")

def delete_employee():
    employee_id = int(input("Enter Employee ID to delete: "))
    employee = session.get(Employee, employee_id)
    if not employee:
        print(f"Employee with ID {employee_id} does not exist.")
        return
    session.delete(employee)
    session.commit()
    print(f"Employee ID {employee_id} deleted successfully.")

def assign_employee():
    employee_id = int(input("Enter Employee ID: "))
    supervisor_id = int(input("Enter the new Supervisor ID: "))
    employee = session.get(Employee, employee_id)
    supervisor = session.get(Supervisor, supervisor_id)
    if not employee or not supervisor:
        print("Invalid Employee ID or Supervisor ID.")
        return
    employee.supervisor_id = supervisor_id
    session.commit()
    print("Supervisor assigned successfully.")

def list_supervisors():
    supervisors = session.query(Supervisor).all()
    if not supervisors:
        print("No Supervisors found.")
    for supervisor in supervisors:
        print(supervisor)

def list_employees():
    employees = session.query(Employee).all()
    if not employees:
        print("No Employees found.")
    for employee in employees:
        print(employee)

def view_employees_by_supervisor():
    supervisor_id = int(input("Enter Supervisor ID to view employees: "))
    supervisor = session.get(Supervisor, supervisor_id)
    if not supervisor:
        print(f"Supervisor with ID {supervisor_id} does not exist.")
        return
    employees = supervisor.employees
    if not employees:
        print(f"No employees found for Supervisor with ID {supervisor_id}")
        return
    print(f"Employees under Supervisor '{supervisor.name}' (ID {supervisor_id}):")
    for employee in employees:
        print(employee)

def create_duty():
    description = input("Enter duty description: ")
    employee_id = int(input("Enter Employee ID: "))
    employee = session.get(Employee, employee_id)
    if not employee:
        print(f"Employee with ID {employee_id} does not exist.")
        return
    duty = Duty(description=description, employee_id=employee_id)
    session.add(duty)
    session.commit()
    print(f"Duty '{description}' created with ID {duty.id} and assigned to Employee ID {employee_id}")

def list_duties():
    duties = session.query(Duty).all()
    if not duties:
        print("No duties found.")
    for duty in duties:
        print(duty)

def delete_duty():
    duty_id = int(input("Enter Duty ID to delete: "))
    duty = session.get(Duty, duty_id)
    if not duty:
        print(f"Duty with ID {duty_id} does not exist.")
        return
    session.delete(duty)
    session.commit()
    print(f"Duty ID {duty_id} deleted successfully")

def view_duties_by_employee():
    employee_id = int(input("Enter Employee ID to view duties: "))
    employee = session.get(Employee, employee_id)
    if not employee:
        print(f"Employee with ID {employee_id} does not exist.")
        return
    duties = employee.duties
    if not duties:
        print(f"No duties found for Employee with ID {employee_id}")
        return
    print(f"Duties assigned to Employee '{employee.name}' (ID {employee_id}):")
    for duty in duties:
        print(duty)


def main_menu():
    while True:
        print("\nWelcome to the Application. What would you like to do?")
        print("1. Create Supervisor")
        print("2. Update Supervisor")
        print("3. Delete Supervisor")
        print("4. Create Employee")
        print("5. Update Employee")
        print("6. Delete Employee")
        print("7. Assign Employee to Supervisor")
        print("8. List Supervisors")
        print("9. List Employees")
        print("10. View Employees by Supervisor")
        print("11. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_supervisor()
        elif choice == "2":
            update_supervisor()
        elif choice == "3":
            delete_supervisor()
        elif choice == "4":
            create_employee()
        elif choice == "5":
            update_employee()
        elif choice == "6":
            delete_employee()
        elif choice == "7":
            assign_employee()
        elif choice == "8":
            list_supervisors()
        elif choice == "9":
            list_employees()
        elif choice == "10":
            view_employees_by_supervisor()
        elif choice == "11":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    init_db()
    main_menu()

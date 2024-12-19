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






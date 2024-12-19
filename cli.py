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







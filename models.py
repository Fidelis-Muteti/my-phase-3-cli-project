from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Supervisor(Base):
    __tablename__ = "supervisors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # One-to-many relationship: a supervisor can have many employees
    employees = relationship("Employee", back_populates="supervisor", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Supervisor(id={self.id}, name='{self.name}', email='{self.email}')"

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    supervisor_id = Column(Integer, ForeignKey("supervisors.id"))

    # Many-to-one relationship: an employee has one supervisor
    supervisor = relationship("Supervisor", back_populates="employees")

    def __repr__(self):
        return f"Employee(id={self.id}, name='{self.name}', age={self.age}, supervisor_id={self.supervisor_id})"

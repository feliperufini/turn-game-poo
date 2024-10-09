# ----------------------------------------------------------------------
# POO

# Classe
class Person:
  def __init__(self, name: str, age: int) -> None:
    self.name = name
    self.age = age

  def hello(self):
    return f"Olá, meu nome é {self.name} e eu tenho {self.age} anos."

# Object
person1 = Person("John Doe", 30)
person2 = Person("Jane Smith", 25)

print(person1.hello())
print("Nome:", person1.name)
print("Idade:", person1.age)

# Herança
class Employee(Person):
  def imEmployee(self):
    return "Eu sou um funcionário."

employee1 = Employee(name="Joana Dark", age=31)
print(employee1.hello())
print(employee1.imEmployee())

# ----------------------------------------------------------------------
# Abstract

from abc import ABC, abstractmethod

class Veichle(ABC):
  @abstractmethod
  def start(self):
    pass

  @abstractmethod
  def stop(self):
    pass

class Car(Veichle):
  def __init__(self) -> None:
    pass

  def start(self):
    return "Carro ligado."

  def stop(self):
    return "Carro desligado."

car1 = Car()
print(car1.start())
print(car1.stop())

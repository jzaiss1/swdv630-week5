# John Zaiss (GitHub id jzaiss1)
# SWDV 630: OBJECT-ORIENTATED CODING 1W 20/SP1
# Week 5 Assignment - Patterns (Abstract Factory)

from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
  def __init__(self, name, ssn):
    # TODO Create ID Generator self.id = createID() 
    self.name = name
    self.hired = ""
    self.terminated = ""
    self.ssn = ssn # TODO Add a validator
    self.active = False

  def status(self):
    if self.active:
      return "active"
    else:
      return "not active"

  @abstractmethod
  def get_position(self):
      pass

  def __str__(self):
    return "{} is a {} and is {} ".format(self.name, self.__class__. __name__,  self.status())

class Cashier(Employee):
  def get_position(self):
    return "cashier"

class Manager(Employee):
  def get_position(self):
    return "management"

class InvManager(Employee):
  def get_position(self):
    return "inventory manager"

class EmployeeFactory(object):
  @classmethod
  def create(cls, name, *args):
    name = name.lower().strip()

    if name == 'cashier':
      return Cashier(*args)
    elif name == 'manager':
      return Manager(*args)
    elif name == 'inventory manager':
      return InvManager(*args)

def main():
  factory = EmployeeFactory()
  print (EmployeeFactory.create('cashier', 'Tracy', '123-45-6789'))
  print (EmployeeFactory.create('inventory manager', 'William', '123-45-6789'))

main()
# Inheritance = Allows a class to inherit attributes and methods from another class helps with code reusability and extensiblility class child (parent)
class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep (self):
        print(f"{self.name} is sleeping")
class Cat(Animal):
# class defintion can't be empty  so to avoid any error we use pass statement
      pass
class Mouse(Animal):
      pass
cat = Cat("meow")
mouse = Mouse("Micky")
print(cat.name)
print(mouse.name)
cat.sleep()
# object: A "bundle" of realted attributes (variable) and methods(functions)
# Ex: phone, cup, book
# You need a "class: to create many objects
# class = (blueprint) used to design the structure and layout of an object
#constructor is a dunder method that is double score method
class Car:
#constructor is similar to functions and this method is used to create objects and default constructor argument is self
      def __init__(self,model,year,color,for_sale):
          self.model = model
          self.year = year
          self.color = color
          self.for_sale = for_sale


      def drive(self):
               print(f"you drive the {self.model}")


      def stop(self):
              print(f"You stop the {self.model}")
      def describe(self):
                  print(f"My favourite car {self.model}")

# in the output the memory address of object is given:<__main__.Car object at 0x000001AD550A6900>
#Objects can also contain methods. Methods in objects are functions that belong to the object.



class Employee:
    __salary = 5000

    def increment(self):
        self.__salary += 10000

    def deduct(self):
        self.__salary -= 5000
    
    def get_salary(self, name):
        print(f"salary of {name} is {self.__salary}")

a = Employee()
a.increment()
a.deduct()
a.get_salary("anuj")

a = Employee()
a.increment()
a.deduct()
a.get_salary("Raj")
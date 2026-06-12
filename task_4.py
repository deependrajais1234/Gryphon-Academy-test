class Age_Verification:
        def __init__(self, age):
            self.age = age

        def set_age(self):
            try:
                if self.age<0:
                    print("valid age")

                if self.age<18:
                    print("valid age")

                if self.age>100:
                    print("valid age")
        
            except ValueError:
                 print("age should be above 0")
            except UnderAgeError:
                 print("age should be above 18")

            except InvalidAgeError:
                 print("age should be less than 100")


age = int(input("Enter your age: "))
a = Age_Verification(age)
a.set_age()
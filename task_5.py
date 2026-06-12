class login_System:
    __password = 'python@123'
    __attempts = 3

    def login(password):
        try:
            if password != self.__password:
                attempts -=1
                print(f"Entered wrong password! Remaning attemps are {attempts}")
            
            else:
                print("Loging successful")

        
            if attempts == 0:
                    raise AccountLockedError("Account has been locked.")
        except Exception as e :
             print(e)

password = int(input("enter you password"))
a = login_System()
a.login(password)
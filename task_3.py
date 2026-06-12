class Father:
    def propery(self):
        print("my propery")

    def business(self):
        print("my business")

class Son(Father):
    def study(self):
        print("study using Father  money")

class Daughter(Father):
    def dance(self):
        print("going for dance class")        

class GrandChild(Son,Daughter):
    def gaming(self):
        print("playing alot of games")


a = GrandChild()
a.propery()
a.business()
a.study()
a.dance()
a.gaming()
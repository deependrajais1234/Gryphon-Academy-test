
from abc import ABC, abstractmethod
class Vehicle:


    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def fule_type(self):
        pass 


class Car(Vehicle):

    def start(self):
        print("Car started")

    def stop(self):
        print("car stoped")
    
    def fule_type(self):
        print("Petrol")

class Bike(Vehicle):

    def start(self):
        print("bike started")

    def stop(self):
        print("biek stoped")
    
    def fule_type(self):
        print("Petrol")

class Tesla(Vehicle):

    def start(self):
        print("Tesla started")

    def stop(self):
        print("Tesla stoped")
    
    def fule_type(self):
        print("Elextric")

c = Car()
c.start()
c.fule_type()


b = Bike()
b.start()
b.fule_type()


t = Tesla()
t.start()
t.fule_type()
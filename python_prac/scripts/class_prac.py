import numpy as np

class Env:
    def __init__(self, name, age, address):
	self.hello = 'Hello'
	self.name = name
	self.age = age
	self.address = address

    def greeting(self):
	print('{0} my name is {1}.'.format(self.hello, self.name))

    def hello(self):
	self.greeting()

if __name__ == "__main__":
     print("Not imported")
else:
     print("Imported")


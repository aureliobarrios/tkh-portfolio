# TODO: implement Fellow class that inherits from "Person"
# we just include another method called "form_group()"
# that prints out all the people that this fellow knows
# using a for-loop. Implement below
from Person import PersonClass

class Fellow(PersonClass):
    def form_group(self):
        print(self.name + " knows these people")
        for person in self.aff:
            print(person)


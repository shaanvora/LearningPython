""" I created a name class to see how special/magic functions work"""


class NameList:

    def __init__(self):
        self.namelist = {}

    def __call__(self, first, last):
        self.namelist[first] = last
        return self.namelist

    def __str__(self):
        return str(self.namelist)

newlist = NameList()

newlist('Joe', 'Blow')
newlist('Billy', 'Bob')

print(newlist)
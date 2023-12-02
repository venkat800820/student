class student:
    def  __init__(self,rn,name):
        self.name=name
        self.rn=rn
    def display(self):
        print("The name of the studentis",self.name)
        print("The roll no of student is",self.rn)   
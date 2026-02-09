#create class employee with method info and 2 attributes

class emp():
    emp_name ="Parth"
    emp_dept="IT"

    def info(self,emp_name,emp_dept): #mandatory parameter
        print(f"Employee {self.emp_name} works for {self.emp_dept}")
        print(f"Employee {emp_name} works for {emp_dept}")

#create object now

emp1 = emp()
print(emp1.emp_name)

#emp1.info() -> it will give an error if we doesnt mention self in method including the attributes

emp1.info("ParthAhuja","CS")

class empInfo():
    company_name ="XYZ"

    def __init__(self):
        print("constructor")
    
    def info(self):
        print(f"Employee {self.emp_name} works for {self.emp_dept}")

emp2 = empInfo()


class empInfo():
    company_name ="XYZ"

    def __init__(self,empName,empDept):
        self.empName = empName
        self.empDept = empDept

    #It is not recommended
    def changes(self, new_company):
        self.company_name=new_company

    #Industrial implementation 
    @classmethod
    def changesInClass(cls, new_company):
        cls.company_name=new_company
    
    def info(self):
        print(f"Employee {self.empName} works for {self.empDept}")
    
    @staticmethod #--> if it will not be passed then there will be issue in passing the arguments
    def addition(x,y):
        print(x+y)

emp2 = empInfo("parth","IT")
emp2.info()

emp2.addition(1,2)
        
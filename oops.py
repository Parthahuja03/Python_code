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
    
    def info(self):
        print(f"Employee {self.empName} works for {self.empDept}")

emp2 = empInfo("parth","IT")
emp2.info()
        
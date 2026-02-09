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
    
    #act as a getter
    @property
    def info(self):
        print(f"Employee {self.empName} works for {self.empDept}")
    
    @info.setter
    def info(self, new_empDetails):
        self.empName=new_empDetails[0]
        self.empDept=new_empDetails[1]

    
    @staticmethod #--> if it will not be passed then there will be issue in passing the arguments
    def addition(x,y):
        print(x+y)

    #act as a setter 
    def changeInfo(self, new_empName, new_empDept):
        self.empName=new_empName
        self.empDept=new_empDept

'''emp1 = empInfo("Parth","IT")
emp1.info()
emp1.changeInfo("ParthAhuja", "CS")
emp1.info()'''

emp1 = empInfo("Parth","IT")
emp1.info =["parthAhuja", "CS"]#--> Setter

print(emp1.info)#-->Getter
class Employee:
    # Declaring variable inside the class directly - Static variable
    Company_name = 'AstraZeneca'
    def __init__(self,empname,empno,empdes):
        # Declaring variables with self, instance variable
        self.empname = empname
        self.empno = empno
        self.empdes = empdes

    def method1(self):
        # Declaring Variables inside method locally without self is known as Local variable
        Projects_completed = 5
        print(f"Totally {Projects_completed} projects are completed by the employee {self.empname}")

obj1 = Employee("Hariharan",121,"Associate Consultant")
print(obj1.method1())

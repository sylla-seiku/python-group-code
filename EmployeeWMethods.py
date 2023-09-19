class EmployeeWMethods:
    def __init__(self, empID, empName, empDept, empSalary):
        self._empID = empID
        self._empName = empName
        self._empDept = empDept
        self.empSalary = empSalary # Let's use the setter here
    # Just one property - wanna keep this short
    @property
    def empSalary(self):
        return self._empSalary

    @empSalary.setter
    def empSalary(self, new_val):
        self._empSalary = None
        if 30_000 <= new_val <= 200_000:
            self._empSalary = new_val
        else:
            print(f"Passed value of {new_val} not in range. Salary set to 'None'")
    # Give employee a raise: pct must be between 10 and 20 pct
    # and resulting salary must be in bounds coded in setter or 200K whichever is less
    def give_emp_pct_raise(self, pct):
        if self._empSalary is None:
            print(f'Employee with ID = {self._empID} has no valid salary - no change made')
        elif pct < 10 or pct > 20:
            print(f'Raise percentage {pct} out of range – no change made')
        else:
            self._empSalary *= (1 + pct/100)
            if self._empSalary > 200_000:
                self._empSalary = 200_000
                
    # Print a representation of an Employee object
    def print_me(self):
        print(f"Info for Employee with ID = {self._empID}")
        print(f'Name: {self._empName}\tDepartment: {self._empDept}\tSalary: {self._empSalary:,.2f}')
 
if __name__ == "__main__":       
    an_emp = EmployeeWMethods(123, "Lou", "D11", 123_456)
    # Print employee salary
    print(f'From Class: {an_emp.empSalary = }')
    # Give raise, print again
    an_emp.give_emp_pct_raise(20)
    print(f'From Class: {an_emp.empSalary = }')
    print(f'{an_emp.empSalary}')
    # Print employee particulars
    an_emp.print_me()    
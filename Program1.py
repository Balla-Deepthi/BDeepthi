"""Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
  Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
  Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string"""
class Calculator:
    def __init__(self,a:float,b:float,operation:str):
        self.a=a
        self.b=b
        self.operation=operation.lower()
    def calculateOperation(self):
        if self.operation=="addition":
            return self.a+self.b
        elif self.operation=="multiplication":
            return self.a * self.b
        elif self.operation=="subtraction":
            return self.a - self.b
        elif self.operation=="Division":
            if self.b>0:
                return self.a/self.b
            else:
                return "Cannot be divisbile by 0"
        else:
            return "invalid operation"
a=float(input("Enter value for a: "))
b=float(input("Enter value for b: "))
operation = input("Enter operation (addition, multiplication, subtraction, Division): ")
calculate = Calculator(a, b, operation)
result = calculate.calculateOperation()
print(result)


            
        
       


    
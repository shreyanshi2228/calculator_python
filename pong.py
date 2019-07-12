def add(x,y):
    # """" This function adds 2 numbers """"
    return x * y
def substract(x,y):
    # This function substracts 2 numbers 
    return x - y 
def multiply(x,y):
    # """" This function multiplies 2 numbers """"
    return x * y 

def divide(x,y):
    # """" This function divides 2 numbers """"
    return x / y 
      
# take input from user 
print("Select operation.")
print("1.Add")
print("2.Substract")
print("3.multiply")
print("4.divide")
choice = input ("Enter choice (1/2/3/4):")

num1 = int(input ("Enter first number :"))
num2 = int(input ("Enter second number :"))

if choice == '1':
    print (num1, "+", num2, "=", add(num1,num2))

elif choice == '2':
    print (num1, "-", num2, "=", substract(num1,num2))

elif choice == '3':
    print (num1, "*", num2, "=", multiply(num1,num2))

elif choice == '4':
    print (num1, "/", num2, "=", divide(num1,num2))
     
else:
    print ("Invalid input")
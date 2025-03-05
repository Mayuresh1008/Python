# Defining the function
def hello_world():
    print("Hello World!")
    
# calling the function
hello_world()

# Defining functions with parameters , Parameters can't be changed
def sum(num1=0, num2=0): 
    # Default parameters value are assigned at the time of function definition if not provided at the time of function call
    # print(num1 + num2)
    if type(num1) is not int or type(num2) is not int:
        return 0
    return num1 + num2

# calling the function with arguments, Arguments can be changed
# sum(9, 8)
# sum(1, 7)
# sum(100, 3)

total = sum()
print(total)

def mulitple_items(*args): 
    # *args is a variable length argument, it can take any number of arguments and it is used when we don't know how many arguments will be passed to the function
    print(args)
    print(type(args))

mulitple_items("Dave", "John", "Sara")

def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))
    # **kwargs is a variable length keyword argument, it can take any number of keyword arguments and it is used when we don't know how many keyword arguments will be passed to the function

multi_named_items(first="Dave", last="Gray")



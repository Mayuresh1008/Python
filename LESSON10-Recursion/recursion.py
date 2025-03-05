# Recursive Function
def add_one(num):
    
    if num >= 9:
        return num + 1
    
    total = num + 1
    print(total)
    
    return add_one(total)

# add_one(0) # only prints till 9
mynewtotal = add_one(0) # storing the function value in a variable if we want to get the return value 
print(mynewtotal) # prints till 10
    
# Same output using loops
# def add_one(num):
#     while True:
#         if num >= 9:
#             return num + 1
#             break
#         num += 1
#         print(num)

# mynewtotal = add_one(0)
# print(mynewtotal)

# While loop
# value = 1

# Using break
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# Using continue
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))
    
# for loop
# names = ["Dave", "Sara", "John"]
# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Sara":
#         # break
#         continue
#     print(x)

# for x in range(4): # 0, 1, 2, 3
#     print(x)
    
# for x in range(2,4): # 2, 3
#     print(x)
    
# for x in range(0, 100, 5): # 0, 5, 10, 15, 20, 25, and so on
#     print(x)
# else:
#     print("Glad that\'s over!")
    
# Nested loops
    
names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")
        
for action in actions:
    for name in names:
        print(name + " " + action + ".")
        

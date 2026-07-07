# Demonstrating the type() function

print(type(10))
print(type(10.5))
print(type(True))
print(type("hello"))

# Question 2

# Demonstrating operator precedence

result = 3 + 4 * 2 ** 2 - 1

print("Result =", result)

# Question 3
# Demonstrating between continue and break

print("using continue:")

for i in range (1, 11):
    if i == 5:
        continue
    print(i)

print("\nUsing break:")

for i in range(1, 11):
    if i == 5:
        break
    print(i)
    

x = 5
y = "John"
print(x)
print(y)

print(type(x))
print(type(y))

print(str(x)+y)  #can't to print(x+int(y))


x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

a = "Hello"
try:
    a = int(input("Enter a number: "))
except ValueError:
    print("Not an integer value...")
print(str(a))
import os

a = int(os.getenv("NUMBER1", 10))
b = int(os.getenv("NUMBER2", 20))

print("Sum of the two numbers:", a + b)

import random

password_generator = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+><.,:}{|~`"
password_length = int(input("Enter the Length of the password:"))
a = "".join(random.sample(password_generator,password_length))
print(f"Your Password is : {a}")
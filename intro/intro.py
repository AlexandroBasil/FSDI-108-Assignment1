print("Hello from python")

# *Single line commen

# *variables and variable types

name = "Basil"

age = 27
total = 20.35
found = True


print(age)
print(total)
print(found)
print(name + name) # *string concatenation
print(age + 1) # *sum
print(name + str(age))


if(age < 100):
    print("You're stil young")
    print("Believe it")
elif (age == 100):
    print("Now that's old!")
else:
    print("Oldy pants")


print("This will print outside of if")


def test():
    print("Hello, I'm a test")


test()  # *Call / execute function
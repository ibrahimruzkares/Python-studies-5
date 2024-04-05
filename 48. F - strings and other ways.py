name = "Mike"
age = 25

print("Hello my name is" + " " + name +  " " + "and I am" + " " + str(age) + " " + "years old.")
print("Hello my name is %s and I am %d years old." %(name,age))
print("Hello my name is {} and I am {} years old.".format(name,age))

print(f"Hello my name is {name} and I am {age} years old.")

print(f"Hello my name is {name} and I am {age if age % 2 == 0 else 7} years old.")
test = 'Whatsup'
testint = int(test)
print(type(test))
print(type(testint))
# Here, it shows error as 'Whatsup' is a string and on using function int on the test, it can't be
# converted to an integer.

# Only an integer in string, can be converted into an integer using "int" function,
# whereas words like Hello, Whatsup can't be converted into integer using "int" function.
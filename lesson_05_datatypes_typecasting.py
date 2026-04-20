#Lesson 5: Datatypes & Typecasting
  #Datatypes - Data types specify the kind of value a variable holds.
  #Common Data Types: 
"""
1. Integer (int)
Whole numbers
x = 10

2. Float (float)
Decimal numbers
y = 3.14

3. String (str)
Text (inside 2 quoutation marks " or ')
name = "John"

4. Boolean (bool)
True or False
is_student = True

5. List
Collection of values
nums = [1, 2, 3]

"""
# Classify these types of statements:

# print(type('hello'))  = STRING
# print(type(1))        = INTEGER
# print(type(1.64))     = FLOAT
# print(type(True))     = BOOLEAN

#Check Data Type: print(type(x))
  # Typecasting - Typecasting is the process of converting one data type into another to avoid errors when performing operations on different data types.
"""
Common Conversions:
➤ String to Integer
x = "10"
x = int(x)

➤ String to Float
x = "3.5"
x = float(x)

➤ Number to String
x = 100
x = str(x)

"""

#TYPECASTING / chaning a type. ex: integer - string
#Original
print('Your son ' + name + ' is failing ' + failed_subjects + ' subjects.')
print(name + '  will need to redo ' + failed_subjects + '  courses.')

#Updated
print('Your son ' + name + ' is failing ' + str(failed_subjects) + ' subjects.')
print(name + '  will need to redo ' + str(failed_subjects) + '  courses.')

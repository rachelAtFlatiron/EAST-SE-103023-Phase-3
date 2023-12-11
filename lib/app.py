#!/usr/bin/env python3

import ipdb

# Pipfile -> package.json
# Pipfile.lock -> package-lock.json
# pipenv install -> npm install
# pipenv package binaries (bin) are stored in another part of your file system -> node_modules 
# pipenv shell -> kind of like npm start but not really 

# Data Types
 
# ints, floats, strings, booleans,  dictionaries (JS: objects), lists (JS: arrays), sets, tuples
# test datatypes: type()
# booleans: JS => true, Python => True
# casing: JS => camelCase, Python => snake_case 
# testing for equality: JS => ===, Python => == 
# null values: JS => null, Python => None
# printing values: JS => console.log(), Python => print() 
# interpolating strings: JS => console.log(`${someVar}`), 
#   Python => print(f'{some_var}')
# line breaks/creating scope: JS => { }, Python => manual indentation 
# declaring variables: JS => can declare variables without assignment (let someVar)
# declaring variables: JS => let, const, var, Python => no let, const, var
#   Python => have to declare a variable with assignment
# if/else: JS => if(){...} else {...}, 
#   Python: 
#       if():
#           proper indentation
#       else:
#           proper indentation
# functions: JS => function func(){...}
#   Python:
#       def func():
#           proper indentation 
# exceptions: JS => try...catch..., Python => try...except...
#   allows us to create custom error messages based on error type (https://docs.python.org/3/library/exceptions.html)

#✅ 1. Create a condition to check a pet's mood
    # If "pet_mood" is "Hungry!", "Rose needs to be fed."
    # If "pet_mood" is "Rowdy!", "Rose needs a walk."
    # In all other cases, "Rose is all good."
pet_mood = "Rowdy!"
pet_name = "Momo"
global_pet = "Odie"

if pet_mood == "Hungry!": 
   print(f'{pet_name} needs to be fed.') 
elif pet_mood == "Rowdy!":
   print(f'{pet_name} needs a walk.')
else: 
   print(f'{pet_name} is all good.')

#✅ 2. Create a ternary operator using "pet_mood" as a condition:
# JS => condition ? true : false
# Python => "If True" if "Condition" else "If False"
print(f'{pet_name} needs to be fed.' if pet_mood == "Hungry!" else print(f'{pet_name} is all good.'))
print(f'{pet_name} needs a walk.') if pet_mood == "Rowdy!" else print(f'{pet_name}  is all good.')

#✅ 3. Create a function (say_hello) that returns the string "Hello, world!"
def say_hello():
   return "Hello, world!" 

# say_hello_with_params()
# can put parameters out of word on invocation as long as you put param=
def say_hello_with_params(param="default", greeting="Howdy"):
   return f"{greeting}, {param}!"
# say_hello_with_params(greeting="Hello", param="world")

#✅ 4. Create a function (pet_greeting) that will return a string with interpolated pet's name
def pet_greeting():
   #can update global variables in fxns, however this value won't persist outside of pet_greeting
   # UNLESS you explicitly call it the global variable
   global global_pet 
   global_pet = "global_Odie"

   pet_name = "Pierre"
   return f"{pet_name} says hello!"
print(pet_name) #pet_name is still "Momo"
print(global_pet) #global_pet is changed to "global_Odie" after invoking pet_greeting()

#✅ 5. Move conditional logic from Deliverable 1 into a function (pet_status) so that we may use it with different pets / moods
def pet_status(pet_name, pet_mood):
    if pet_mood == "Hungry!": 
        return(f'{pet_name} needs to be fed.') 
    elif pet_mood == "Rowdy!":
        return(f'{pet_name} needs a walk.')
    else: 
        return(f'{pet_name} is all good.')

#✅ 6. Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
    # If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
    # pet_birthday(10) => "Happy Birthday! Your pet is now 11."
    # pet_birthday("oops") => "Type Error Occurred"
def pet_birthday(age):
   try: 
      new_age = age + 1 
      print(sdlkfj) #print something that doesn't exist to trigger name error
      return f"your pet is now {new_age}"
    
   except TypeError: #pass in string instead of int to trigger errors
      return "age must be an integer"
   except NameError: 
      return "Name Error Occurred"


ipdb.set_trace() #breakpoint (stop code from executing here)
#type c to continue execution
#ctrl + D to exit 


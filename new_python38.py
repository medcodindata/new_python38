
#********* The walrus operator  ':='  *******#
# This means that you can assign a value to a variable in a task at the same time

# Example 1 :
# With walrus operator :
for i in range(a:=5):
    print("a =",a, ",i =",i) # => a = 5

# Without walrus operator :
a = 5
for i in range(a):
    print("a =", a, ",i =", i) # => a = 5


# Example 2 :
data = [
     {"task_id": 2, "status": 'Pending'},
     {"task_id": 3, "status": 'Done'},
     ]
# With walrus operator
for row in data:
    if status := row.get("status"):
        print(status)          # => Pending, Done

# Without walrus operator :
for row in data:
    status = row.get("status")
    if status :
        print(status)          # => Pending, Done

#*********  Positional-only parameters to improve the python consistency *********#
# In the following example, parameters a is positional-only,
# while b can be positional or keyword, and c is required to be keywords

def func(a, /, b,  *, c):
    return a, b, c

print(func(10, 20, c = 30))     # => (10, 20, 30) here you should indicate the 'c='
print(func(10, b = 20, c = 30)) # => (10, 20, 30) b can a keyword too because of the '/'
print(func(10, 20, 30))  # => error : 'TypeError: func() takes 2 positional arguments but 3 were given'
# Indeed, because we have only a and b as positional parameter

#********* f-strings support '=' for self-documenting expressions and debugging *********#
a = 4
b = 5
print(f'{a = } , {b = }')   # => a = 4 , b = 5
print(f'{a = } , {b+3 = }') # => a = 4 , b+3 = 8

# ***************** end ***********









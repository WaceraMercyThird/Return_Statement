# Escaping character
# form feed
x = 'Fruit'
print(f'{x} juice')


# return statement
def cube(num):
    return num*num*num

print(cube(2)) 

# booleans
is_students = True
is_tall = False

if is_students and is_tall:
    print("You are a male")
else:
        print("You are not a student")


if is_students or is_tall:
    print("You are a male")
else:
        print("You are not a student")
# else is_students and not (is_tall)

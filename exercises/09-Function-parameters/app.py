# Your code goes here:
def render_person(name, dob, eyecolor, age, gender):
    phrase = (f'{name} is a {age} years old {gender} born in {dob} with {eyecolor} eyes')
    return phrase


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))
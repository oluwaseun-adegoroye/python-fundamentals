#Variables and date type
name = input('What is your name?').strip().title()
age = int(input('How old are you?'))
height = float(input('Height in meter?'))

print(f'Hello {name}')
print(f'You are {age} years old')
print(f'You are {height}m tall')

#Your age in ten years
future_age = age + 10
print(f'You will be {future_age} in ten years')
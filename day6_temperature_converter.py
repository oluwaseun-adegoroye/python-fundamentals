# Temperature converter

print('=== Temperature Converter ===')
print('1. Celsius to Fahrenheit')
print('2. Fahrenheit to Celsius')
print('3. Celsius to Kelvin')

option = input('Choose one option (1, 2 or 3): ')

if option == '1':
    celsius = float(input('Enter temperature in Celsius: '))
    fahrenheit = (celsius * 9/5) + 32
    print(f'{celsius}°C = {fahrenheit}°F')
elif option =='2':
    fahrenheit = float(input('Enter temperature in Fahenheit: '))
    celsius = (fahrenheit - 32) * 5/9
    print(f'{fahrenheit}°F = {celsius}°C')
elif option == '3':
    celsius = float(input('Enter temperature in Celsius: '))
    kelvin = celsius + 273.15
    print(f'{celsius}°C = {kelvin}K')
else:
    print('Invalid input')
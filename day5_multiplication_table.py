# Multiplication table

n = int(input('Enter the number: '))
print(f'\nMultiplication table for {n}: ')
for i in range(1, 13):
    num = n * i
    print(f'{n} x {i} = {num}')

# Pattern generator
print('\nPattern')
for i in range(1, 6):
    print('*' * i)
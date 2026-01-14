#Grade calculator
score = float(input('Enter your score (0-100): '))
if score >= 70:
    grade = 'A'
    print('Execellent!')
elif score >= 60:
    grade = 'B'
    print('Very Good!')
elif score >= 50:
    grade = 'C'
    print('Fair!')
elif score >= 45:
    grade = 'D'
    print('Pass!')
else:
    grade = 'F'
    print('Fail')

print(f'Your grade is: {grade}')
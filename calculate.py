first_number = input('Type the first number : ')
operator = input('Operation : ')
second_number = input('Type the second number : ')

if operator == '+':
    print(float(first_number) + float(second_number))
elif operator == '-':
    print(float(first_number) - float(second_number))
elif operator == '*':
    print(float(first_number) * float(second_number))
elif operator == '/':
    print(float(first_number) / float(second_number))
else:
    print('Operator not recognized.')

# Dictionnary

months = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December'
}

print('Montacer is born in ' + months.get('Oct'))

obj = {'Foo': 'titi', 'Bar': None}

has_bar = obj['Foo'] or obj['Foo']

print('Result', has_bar)

# List Functions.

luck_numbers = [3, 6, 9, 12]
friends = ['Hermano', 'Ghassen', 'Kais']

luck_numbers.extend(friends)
luck_numbers.append(100)
luck_numbers.insert(5, "El Manifico")
luck_numbers.remove(9)
print("Lucky Numbers ... ", luck_numbers)


# Functions

def say_hi(name):
    print('Hello ' + name + ', Ab3eth Ab3eth.')


def get_cube(number):
    return number * number * number


say_hi('Walid')
print(get_cube(6))

# If statements

is_female = True
is_tall = True

if is_female and is_tall:
    print('Tall Female')
elif is_female and not(is_tall):
    print('Short Female')
else:
    print('Neither Female nor tall')

# While loop

iterator = 0
while iterator <= 6:
    print(iterator)
    iterator += 1
print('Done with While loop.')

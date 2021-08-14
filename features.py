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

# For loop

forloop_list = ['yezzi m laab']

for friend in friends:
    forloop_list.append(friend)

print('forloop_list', forloop_list)


def raise_to_power(base_num, power_num):
    result = 1
    for result in range(power_num):
        result = result * base_num
    return result


print('Raise to power : ', raise_to_power(3, 4))

# Grids

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

luck_num = grid[1][2]

print('My luck Num is : ', luck_num)

# Try Except statement

try:
    div = 2 / 0
    number = int(input('Type a number : '))
    print(number)
except ZeroDivisionError as error:
    print('You just devided by zero ...', error)
except ValueError:
    print('Invalid input ...')

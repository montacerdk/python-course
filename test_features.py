obj = {'foo': 'titi', 'bar': None}

has_bar = obj['foo'] or obj['foo']

print('Result', has_bar)

luck_numbers = [3, 6, 9, 12]
friends = ['Hermano', 'Ghassen', 'Kais']

# List Functions.
luck_numbers.extend(friends)
luck_numbers.append(100)
luck_numbers.insert(5, "El Manifico")
luck_numbers.remove(9)
print("Lucky Numbers ... ", luck_numbers)


def say_hi(name):
    print('Hello ' + name + ', Ab3eth Ab3eth.')


def get_cube(number):
    return number * number * number


say_hi('Walid')
print(get_cube(6))

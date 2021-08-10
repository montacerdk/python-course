obj = {'foo': 'titi', 'bar': None}

has_bar = obj['foo'] or obj['foo']

print('Result', has_bar)

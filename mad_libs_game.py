from string import Template

# Result

print('Roses are red')
print('Violets are blue')
print('Yezzi m laab')

# Mad lib

color_input = input('Type roses color ...')
stuff_input = input('Type blue stuff ...')
name_input = input('Type a gamer name ...')

color_template = Template('Roses are $color')
stuff_template = Template('$stuff are blue')
name_template = Template('Yezzi m laab ya $name')

print(color_template.safe_substitute(color=color_input))
print(stuff_template.safe_substitute(stuff=stuff_input))
print(name_template.safe_substitute(name=name_input))

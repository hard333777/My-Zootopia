import json

with open('animals_data.json', 'r') as file:
    animals = json.loads(file.read())


output = ''
for animal in animals:
    output += f'\nName: {animal['name'].capitalize()}\n'
    if 'diet' in animal['characteristics']:
        output += f'Diet: {animal['characteristics']['diet'].capitalize()}\n'
    if 'locations' in animal:
        output +=f'Location: {', '.join(animal['locations']).title()}\n'
    if 'type' in animal['characteristics']:
        output += f'Type: {animal['characteristics']['type'].capitalize()}\n'

output = output.strip()


with open('animals_template.html', 'r') as file:
    data = file.read()

formatted_data = data.replace('__REPLACE_ANIMALS_INFO__', output)


with open('animals.html', 'w') as file:
    file.write(formatted_data)

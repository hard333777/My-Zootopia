import json

with open('animals_data.json', 'r') as file:
    animals = json.loads(file.read())


output = ''
for animal in animals:
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal['name'].capitalize()}</div>'
    output += '<p class="card__text">'
    if 'diet' in animal['characteristics']:
        output += f'<strong>Diet:</strong> {animal['characteristics']['diet'].capitalize()}<br/>\n'
    if 'locations' in animal:
        output +=f'<strong>Location:</strong> {', '.join(animal['locations']).title()}<br/>\n'
    if 'type' in animal['characteristics']:
        output += f'<strong>Type:</strong> {animal['characteristics']['type'].capitalize()}<br/>\n'
    output += '</p>'
    output += '</li>'




with open('animals_template.html', 'r') as file:
    data = file.read()

formatted_data = data.replace('__REPLACE_ANIMALS_INFO__', output)


with open('animals.html', 'w') as file:
    file.write(formatted_data)

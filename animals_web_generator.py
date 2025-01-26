import json

with open('animals_data.json', 'r') as file:
    animals = json.loads(file.read())


for animal in animals:
    print(f'\nName: {animal['name'].capitalize()}')
    if 'diet' in animal['characteristics']:
        print(f'Diet: {animal['characteristics']['diet'].capitalize()}')
    if 'locations' in animal:
        print(f'Location: {', '.join(animal['locations']).title()}')
    if 'type' in animal['characteristics']:
        print(f'Type: {animal['characteristics']['type'].capitalize()}')


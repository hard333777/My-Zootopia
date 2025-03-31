import json

def serialize_animal(animal_obj):
    """Convert an animal object into an HTML-formatted string for display."""
    try:
        output = ''
        output += '<li class="cards__item">'
        output += f'<div class="card__title">{animal_obj.get('name').capitalize()}</div>'
        output += '<p class="card__text">'
        if 'diet' in animal_obj['characteristics']:
            output += f'<strong>Diet:</strong> {animal_obj.get('characteristics', {}).get('diet').capitalize()}<br/>\n'
        if 'locations' in animal_obj:
            output += f'<strong>Location:</strong> {', '.join(animal_obj.get('locations')).title()}<br/>\n'
        if 'type' in animal_obj['characteristics']:
            output += f'<strong>Type:</strong> {animal_obj.get('characteristics', {}).get('type').capitalize()}<br/>\n'
        output += '</p>'
        output += '</li>'
        return output
    except KeyError:
        print('Impossible to serialize.')


def get_data_for_the_formatting():
    """Read animal data from JSON file and serialize each animal into HTML."""
    try:
        with open('animals_data.json', 'r') as file:
            animals = json.loads(file.read())
        result = ''
        for animal in animals:
            result += serialize_animal(animal)
        return result
    except TypeError:
        print(f"{animal} has the wrong format and was not serialized.")
    except FileNotFoundError:
        print('File was not found.')


def write_html_file(data_for_formatting):
    """Insert formatted animal data into an HTML template and write to a new file."""
    try:
        with open('animals_template.html', 'r') as file:
            data = file.read()


        formatted_data = data.replace('__REPLACE_ANIMALS_INFO__', data_for_formatting)
        with open('animals.html', 'w') as file:
            file.write(formatted_data)
    except FileNotFoundError:
        print('File was not found.')


def main():
    if __name__ == '__main__':
        data_for_formatting = get_data_for_the_formatting()
        write_html_file(data_for_formatting)

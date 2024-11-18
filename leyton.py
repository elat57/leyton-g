import json

def find_word(letter_soup, word):
    rows = len(letter_soup)
    cols = len(letter_soup[0])
    
    directions = [
        (0, 1),   
        (1, 0),   
        (1, 1),   
        (-1, 0),  
        (0, -1),  
        (-1, -1), 
        (-1, 1),  
        (1, -1)   
    ]

  
    def search_from_position(x, y, dx, dy):
        for index in range(len(word)):
            nx, ny = x + index * dx, y + index * dy
            if not (0 <= nx < rows and 0 <= ny < cols) or letter_soup[nx][ny] != word[index]:
                return False
        return True


    for x in range(rows):
        for y in range(cols):
            if letter_soup[x][y] == word[0]: 
                for dx, dy in directions:
                    if search_from_position(x, y, dx, dy):
                        return True  
    return False  

def find_words(letter_soup, words):
    return {word: find_word(letter_soup, word) for word in words}


def generate_report(letter_soup, words, output_path="output.json"):
    results = find_words(letter_soup, words)
    with open(output_path, 'w') as file:
        json.dump(results, file, indent=4)  
    print(f"Reporte generado en: {output_path}")
    return output_path

def read_input_file(file_path):
    try:
        with open(file_path) as file:
            lines = [line.strip() for line in file.read().splitlines()] 
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {file_path}.")
        return [], []
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
        return [], []

    if '---' not in lines:
        print("Error: El archivo no contiene el separador '---'. Asegúrate de que el formato sea correcto.")
        return [], []

    separator_index = lines.index('---')
    letter_soup = [list(line) for line in lines[:separator_index]]
    words = lines[separator_index + 1:]
    return letter_soup, words

try:
    letter_soup, words = read_input_file("input.txt")

    if letter_soup and words:
        generate_report(letter_soup, words)
    else:
        print("No se pudo generar el reporte debido a errores en la entrada.")
except Exception as e:
    print(f"Error crítico: {e}")

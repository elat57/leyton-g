import json

# Función para buscar una palabra en la sopa de letras en todas las direcciones
def find_word(letter_soup, word):
    rows = len(letter_soup)
    cols = len(letter_soup[0])
    
    # Todas las direcciones posibles para buscar (horizontal, vertical, diagonal)
    directions = [
        (0, 1),   # Derecha
        (1, 0),   # Abajo
        (1, 1),   # Diagonal abajo-derecha
        (-1, 0),  # Arriba
        (0, -1),  # Izquierda
        (-1, -1), # Diagonal arriba-izquierda
        (-1, 1),  # Diagonal arriba-derecha
        (1, -1)   # Diagonal abajo-izquierda
    ]

    # Función auxiliar para verificar si una palabra existe en una dirección específica
    def search_from_position(x, y, dx, dy):
        for index in range(len(word)):
            nx, ny = x + index * dx, y + index * dy
            if not (0 <= nx < rows and 0 <= ny < cols) or letter_soup[nx][ny] != word[index]:
                return False
        return True

    # Buscar la palabra en todas las posiciones de la sopa de letras
    for x in range(rows):
        for y in range(cols):
            if letter_soup[x][y] == word[0]:  # Comienza la búsqueda si la primera letra coincide
                for dx, dy in directions:
                    if search_from_position(x, y, dx, dy):
                        return True  # Palabra encontrada
    return False  # Palabra no encontrada

# Función para buscar varias palabras en la sopa de letras
def find_words(letter_soup, words):
    # Devuelve un diccionario con los resultados para cada palabra
    return {word: find_word(letter_soup, word) for word in words}

# Función para generar un reporte en formato JSON con los resultados
def generate_report(letter_soup, words, output_path="output.json"):
    results = find_words(letter_soup, words)
    with open(output_path, 'w') as file:
        json.dump(results, file, indent=4)  # Guardar resultados en un archivo JSON
    print(f"Reporte generado en: {output_path}")
    return output_path

# Función para leer un archivo de entrada y extraer la sopa de letras y las palabras
def read_input_file(file_path):
    try:
        with open(file_path) as file:
            lines = [line.strip() for line in file.read().splitlines()]  # Limpiar espacios en las líneas
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {file_path}.")
        return [], []
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
        return [], []

    # Verificar si el separador '---' está presente
    if '---' not in lines:
        print("Error: El archivo no contiene el separador '---'. Asegúrate de que el formato sea correcto.")
        return [], []

    # Dividir la sopa de letras y las palabras usando el separador
    separator_index = lines.index('---')
    letter_soup = [list(line) for line in lines[:separator_index]]
    words = lines[separator_index + 1:]
    return letter_soup, words

# Ejemplo de uso:
try:
    # Leer la sopa de letras y las palabras desde un archivo
    letter_soup, words = read_input_file("input.txt")

    # Asegurarse de que se cargaron datos correctamente antes de proceder
    if letter_soup and words:
        # Generar el reporte en un archivo JSON
        generate_report(letter_soup, words)
    else:
        print("No se pudo generar el reporte debido a errores en la entrada.")
except Exception as e:
    print(f"Error crítico: {e}")

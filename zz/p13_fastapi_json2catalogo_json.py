import os
import re
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def parse_filename(filename):
    # Eliminar extensión y guiones bajos finales
    name = os.path.splitext(filename)[0].rstrip("_")

    # Detectar el código al principio del nombre (letras+numeros)
    match = re.match(r'^([A-Za-z]+[0-9]+)([A-Za-z0-9]*)$', name)
    if not match:
        return None, None, None

    co = match.group(1)  # Código, ej: 'Codigo456'
    rest = match.group(2)  # Nombre sin espacios, ej: 'NombreSeparadoPorMayusculas'

    # Separar por mayúsculas
    palabras = re.findall(r'[A-ZÁÉÍÓÚÑ][a-záéíóúñ0-9]*', co + rest)
    codigo_legible = ' '.join(palabras).upper()

    return co + rest, codigo_legible, co.upper()

def process_directory(base_dir):
    resultado = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(('.pdf')):
                full_path = os.path.join(root, file)
                grupo = os.path.basename(os.path.dirname(root))
                sector = os.path.basename(root)

                cod, codigo, co = parse_filename(file)
                if not cod:
                    continue

                resultado.append({
                    "categoria": "libre",
                    "codigo": codigo,
                    "sector": sector,
                    "grupo": grupo,
                    "cod": cod,
                    "co": co
                })
    return resultado

# Directorio raíz a analizar
base_directory = "../public/routers"  # Cambia esto si es necesario

# Procesar y guardar
data = process_directory(base_directory)

with open("../src/components/Catalogo.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("JSON generado correctamente.")

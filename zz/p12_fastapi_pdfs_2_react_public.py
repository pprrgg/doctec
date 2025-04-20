import os
import shutil
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

origen = '/home/pk/Desktop/backend/app/routers'
destino = '../public'

# Ruta completa de destino
destino_completo = os.path.join(destino, 'routers')

# Eliminar la carpeta de destino si existe
if os.path.exists(destino_completo):
    shutil.rmtree(destino_completo)

# Copiar recursivamente la carpeta de origen al destino
shutil.copytree(origen, destino_completo)

for root, dirs, files in os.walk('../public/routers'):
    for file in files:
        if file.endswith('.py'):
            ruta_completa = os.path.join(root, file)
            print(f'Eliminando: {ruta_completa}')
            os.remove(ruta_completa)


    # Eliminar la carpeta 'assets' si existe
    if 'assets' in dirs:
        ruta_assets = os.path.join(root, 'assets')
        print(f'Eliminando carpeta assets: {ruta_assets}')
        shutil.rmtree(ruta_assets)  # Elimina la carpeta 'assets' y su contenido

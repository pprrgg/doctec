import os
import shutil
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

origen = '/home/pk/Desktop/backend/app/routers'
destino = '../public'
destino_completo = os.path.join(destino, 'routers')

# Función para ignorar archivos o carpetas con '.~lock' o '__' en el nombre
def ignore_special_files(dir, files):
    return [f for f in files if '.~lock' in f or '__' in f]

# Eliminar la carpeta de destino si existe
if os.path.exists(destino_completo):
    shutil.rmtree(destino_completo)

# Copiar la carpeta, ignorando los archivos/carpetas que cumplan la condición
shutil.copytree(origen, destino_completo, ignore=ignore_special_files)

# Eliminar archivos .py y la carpeta assets
for root, dirs, files in os.walk(destino_completo):
    for file in files:
        if file.endswith('.py'):
            ruta_completa = os.path.join(root, file)
            print(f'Eliminando: {ruta_completa}')
            os.remove(ruta_completa)

    if 'assets' in dirs:
        ruta_assets = os.path.join(root, 'assets')
        print(f'Eliminando carpeta assets: {ruta_assets}')
        shutil.rmtree(ruta_assets)

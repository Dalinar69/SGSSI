import os
import hashlib

# Función para calcular el hash MD5 de un archivo
def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Función para buscar el archivo con el hash MD5 coincidente
def find_file_by_hash(directory, target_hash):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_md5 = calculate_md5(file_path)
            if file_md5 == target_hash:
                print(f"Archivo encontrado: {file_path} (MD5: {file_md5})")
                return file_path
    print("No se encontró ningún archivo con el hash proporcionado.")
    return None

# Directorio donde están las imágenes
directory = '/home/dalinar/UNI/SGSSI/Labo2/imagen'
# Hash objetivo
target_hash = 'e5ed313192776744b9b93b1320b5e268'

# Buscar el archivo que coincida con el hash
find_file_by_hash(directory, target_hash)

#Abrir stegosuite y elegir la imagen 22 en este caso y extraer 
#"Al Fascismo no se le discute, se le destruye." Buenaventura Durruti
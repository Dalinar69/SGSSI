#!/bin/bash

# Directorio donde están las fotos
DIRECTORIO="imagen"
HASH_OBJETIVO="e5ed313192776744b9b93b1320b5e268"

# Recorremos cada archivo en el directorio imagenes
for archivo in "$DIRECTORIO"/*; do
    # Calculamos el hash MD5 del archivo
    # Este comando devuelve la siguiente salida: el hash MD5 + el nombre del archivo.
    # El comando awk '{print $1}' selecciona solo el hash MD5 sin el nombre del archivo
    hash_actual=$(md5sum "$archivo" | awk '{print $1}')

    # Comprobamos si el hash que introducimos es el mismo que el que estamos buscando
    if [ "$hash_actual" == "$HASH_OBJETIVO" ]; then
        echo "Archivo encontrado: $archivo"
        # Si sabemos que exactamente hay un archivo con el hash, podemos salir del bucle utilizando un break
    fi
done

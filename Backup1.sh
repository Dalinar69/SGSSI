#!/bin/bash

# Definir variables
SRC="$HOME/Escritorio/seguridad"
DEST="/var/tmp/Backups/"
LINK_DEST="$DEST/$(date -d 'yesterday' +%d-%m-%Y)" # Copia de ayer
TODAY=$(date +%d-%m-%Y) # Fecha de hoy
BACKUP_DIR="$DEST/$TODAY"

echo "Origen: $SRC"
echo "Destino: $BACKUP_DIR"
echo "Copia incremental basada en: $LINK_DEST"

# Crear directorio de destino si este no existe
mkdir -p "$BACKUP_DIR"

# Comprobar si existe la copia de ayer para hacer una copia incremental
if [ -d "$LINK_DEST" ]; then
    echo "Copia incremental desde $LINK_DEST"
    rsync -av --link-dest="$LINK_DEST" "$SRC/" "$BACKUP_DIR/"
else
    echo "Copia completa"
    rsync -av "$SRC/" "$BACKUP_DIR/"
fi


#!/bin/bash

# Ruta al archivo de salida
OUTPUT_FILE=~/.config/qtile/themes/environment/targetip.txt

# Función para validar la IP
is_valid_ip() {
    local ip="$1"
    # Verifica si es una IPv4 válida
    [[ "$ip" =~ ^([0-9]{1,3}\.){3}[0-9]{1,3}$ ]] &&
    { 
        IFS=. read -r i1 i2 i3 i4 <<<"$ip";
        [[ $i1 -le 255 && $i2 -le 255 && $i3 -le 255 && $i4 -le 255 ]]
    }
}

# Solicita la IP y el nombre opcional
read -p "Escribe la IP de la máquina objetivo, también puedes escribir el nombre: " input

# Divide la entrada en IP y nombre
ip=$(echo "$input" | awk '{print $1}')
name=$(echo "$input" | awk '{$1=""; print $0}' | sed 's/^ //')

# Verifica si la IP es válida
if is_valid_ip "$ip"; then
    # Si hay nombre, agrega un guión
    if [[ -n "$name" ]]; then
        echo "$ip - $name" > "$OUTPUT_FILE"
    else
        echo "$ip" > "$OUTPUT_FILE"
    fi
    echo "La IP y el nombre se han guardado correctamente en $OUTPUT_FILE."
else
    echo "La IP ingresada no es válida. Asegúrate de escribir una IPv4 correcta."
fi

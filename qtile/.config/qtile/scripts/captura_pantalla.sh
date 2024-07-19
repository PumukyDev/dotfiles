#!/bin/bash

# Elimina el archivo screenshot.png si existe
rm -f /tmp/screenshot.png

# Captura de pantalla y copia al portapapeles
sh -c 'scrot --select --line mode=edge /tmp/screenshot.png && xclip -selection clipboard -t image/png -i /tmp/screenshot.png && echo /tmp/screenshot.png >> /home/Adrian/.cache/greenclip.history'

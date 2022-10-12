from datetime import datetime
from os.path import isdir

ahora = datetime.now()
ahora_es = f"Fecha y hora es: {ahora}"
hoy_es = f"Sólo fecha es: { ahora.strftime('%d de %m del %Y') }"
hoy_std_es = f"Sólo fecha (estándard) es: { ahora.strftime('%Y-%m-%d') }"
es_directorio = f"La ruta '../1_hola.py', es un directorio?: { isdir('../1_hola.py') }"
print(ahora_es)
print(hoy_es)
print(hoy_std_es)
print(es_directorio)
import sys
from collections import Counter
from datetime import datetime, time

filename = sys.argv[1]
fuera_horario = Counter()

hora_inicio = time(8, 0, 0)
hora_fin = time(17, 0, 0)

with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        if "usuario:" in line:
            try:
                partes = line.split()
                fecha_str = f"{partes[0]} {partes[1]}"
                hora = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S").time()

                if hora < hora_inicio or hora > hora_fin:
                    usuario = line.split("usuario:")[1].strip().lower()
                    fuera_horario[usuario] += 1
            except Exception as e:
                print(f"⚠️ Error en línea: '{line}': {e}")

with open(f"{filename}.out", 'w') as out:
    for user, count in fuera_horario.items():
        out.write(f"{user} {count}\n")
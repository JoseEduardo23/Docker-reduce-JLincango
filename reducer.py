import os
from collections import Counter

final_counts = Counter()

splits_dir = "splits"

for file in os.listdir(splits_dir):
    if file.endswith(".out"):
        filepath = os.path.join(splits_dir, file)
        with open(filepath, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 2:
                    user, count = parts
                    try:
                        final_counts[user.lower()] += int(count)
                    except ValueError:
                        print(f"⚠️  Línea ignorada en {file}: '{line.strip()}' (conteo inválido)")
print("Conteo total por usuario:")
for user, count in final_counts.items():
    print(f"{user}: {count}, veces fuera del horario laboral")
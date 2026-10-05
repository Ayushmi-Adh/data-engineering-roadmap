temps = [21.5, 23.0, 19.8]
temps.append(25.1)
print(temps[0], temps[-1], temps[1:3])

row = {"time": "2026-10-05T10:00", "temp": 21.5}
print(row["temp"])
print(row.get("humidity", "missing"))   # safe lookup

ids = [1, 2, 2, 3, 3, 3]
print(set(ids))          # dedupe
print(2 in set(ids))     # membership
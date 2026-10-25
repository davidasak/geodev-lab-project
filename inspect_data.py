import csv

def inspect_column(filename, column) :
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return {
    "smallest": min(values),
    "largest": max(values),
    "count": len(values),}

result = inspect_column("Road_Network.csv", "length")
result2 = inspect_column("Road_Network.csv", "osm_id")


print('Length:',result)
print('osm_id:',result2)

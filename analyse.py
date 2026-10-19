with open("wards.csv") as f:
    lines = f. readlines ()
total = 0

for line in lines[1:]:
    parts = line.strip() .split(",")
    ward = parts [0]
    area_km2 = float (parts [1])
    if area_km2 > 9:
        size = "large"
    else:
        size = "small"
    total += area_km2

    print(ward, "is", size)

print('Total area is',total,'km2')
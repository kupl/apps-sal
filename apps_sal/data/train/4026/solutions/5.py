def optimum_location(students, locations):
    best = min(locations, key=lambda loc: sum((abs(abs(loc['x'] - x) + abs(loc['y'] - y)) for (x, y) in students)))
    return f"The best location is number {best['id']} with the coordinates x = {best['x']} and y = {best['y']}"

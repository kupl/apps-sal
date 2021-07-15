def optimum_location(students, locations):
    def total_distance(loc):
        x_dist = sum(abs(loc['x'] - x) for x, y in students)
        y_dist = sum(abs(loc['y'] - y) for x, y in students)
        return x_dist + y_dist
    best_loc = min(locations, key=total_distance)
    template = "The best location is number {id} with the coordinates x = {x} and y = {y}"
    return template.format(**best_loc)
    



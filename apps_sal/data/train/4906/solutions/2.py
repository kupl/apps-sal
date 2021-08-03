def traffic_lights(road, n):
    light_cycle = {"R": "RRRRRGGGGGO", "G": "GGGGGORRRRR"}
    lights = {pos: light_cycle[light] for pos, light in enumerate(road) if light in light_cycle}
    car, result = 0, [road]
    for state in range(1, n + 1):
        if car + 1 not in lights or lights[car + 1][state % 11] not in "OR":
            car += 1
        result.append("".join("C" if pos == car else lights[pos][state % 11] if pos in lights else "." for pos in range(len(road))))
    return result

def traffic_lights(road, n):
    k, car, res = 'GGGGGORRRRR', 0, []
    for i in range(n+1):
        lights = [k[(k.index(s) + i) % 11] if s in 'ROG' else '.' for s in road]
        if car < len(road) - 1:
            if i: car += lights[car+1] not in 'RO'
            lights[car] = 'C' 
        res.append(''.join(lights))
    return res


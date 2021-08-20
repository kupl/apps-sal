def shortest_time(n, m, speeds):
    (elevator_speed, open_door, close_door, walk_speed) = speeds
    elevator_time = (abs(m - n) + n - 1) * elevator_speed + open_door * 2 + close_door
    walk_time = (n - 1) * walk_speed
    return min(elevator_time, walk_time)

def shortest_time(n, m, speeds):
    (move_lift, open_door, close_door, move_feet) = speeds
    healthy = (n - 1) * move_feet
    lazy = abs(n - m) * move_lift + open_door + close_door + (n - 1) * move_lift + open_door
    return min(healthy, lazy)

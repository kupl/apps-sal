def psion_power_points(l, s): return [0, 2, 6, 11, 17, 25, 35, 46, 58, 72, 88, 106, 126, 147, 170, 195, 221, 250, 280, 311, 343][min(l, 20)] + (s - 10) // 2 * l // 2 if l and s > 10 else 0

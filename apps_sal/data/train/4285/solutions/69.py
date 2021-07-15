find_slope = lambda points: str((points[3]-points[1]) // (points[2]-points[0])) if points[2]-points[0] != 0 else 'undefined'

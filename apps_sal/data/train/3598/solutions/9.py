def plane_seat(a):
    return {f'{row}{seat}': f'{end}-{side}' for (end, rows) in [('Front', list(range(1, 21))), ('Middle', list(range(21, 41))), ('Back', list(range(41, 61)))] for row in rows for (side, seats) in [('Left', 'ABC'), ('Middle', 'DEF'), ('Right', 'GHK')] for seat in seats}.get(a, 'No Seat!!')

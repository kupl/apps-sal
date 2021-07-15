def is_magical(sq):
    return sum(sq[2:7:2])==sum(sq[::4])==sum(sq[::3])==sum(sq[1::3])==sum(sq[2::3])==sum(sq[:3])==sum(sq[3:6])==sum(sq[6:])

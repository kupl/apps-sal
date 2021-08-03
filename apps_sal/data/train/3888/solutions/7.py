def clock_degree(s):
    hh, mm = list(map(int, s.split(':')))
    if not (0 <= hh < 24 and 0 <= mm < 60):
        return 'Check your time !'
    hh %= 12
    def fix_zero(theta): return theta if theta != 0 else 360
    return f'{fix_zero(hh * 30)}:{fix_zero(mm * 6)}'

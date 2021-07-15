def can_i_play(now, start, end):
    if end < start:
        start %= 12
        end += 12
        now = 12 if now == 0 else now % 12
        
    return now >= start and now + 1 <= end

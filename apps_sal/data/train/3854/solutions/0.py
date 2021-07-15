def candidates(ymd):
    y, m, d = ymd.split('-')
    return {ymd, f'{y}-{d}-{m}'}

def check_dates(records):
    result = [0, 0, 0]
    for start, end in records:
        xs = [(dt1, dt2) for dt1 in candidates(start) for dt2 in candidates(end)
              if dt1 <= dt2 and dt1[5:7] <= '12' >= dt2[5:7]]
        i = 2 if len(xs) > 1 else xs[0] != (start, end)
        result[i] += 1  # 2: uncertain, 1(True): recoverable, 0(False): correct
    return result

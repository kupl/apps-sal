def draw(waves):
    wave = []
    while sum(waves)!=0:
        black = max(waves)
        cur = ''
        for i in range(len(waves)):
            if waves[i]<black:
                cur += '□'
            else:
                cur += '■'
                waves[i] -= 1
        wave.append(cur)
    return '\n'.join(wave)

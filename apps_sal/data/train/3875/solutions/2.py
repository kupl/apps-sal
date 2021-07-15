ON = '■'
OFF = '□'

def draw(waves):
    result = ''
    height = max(waves)
    for line in range(height, 0, -1):
        for wave in waves:
            if wave >= line:
                result += ON
            else:
                result += OFF
        result += '\n'
    return result.strip()

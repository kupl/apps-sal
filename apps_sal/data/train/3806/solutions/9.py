def black_and_white(height, width, compressed):
    answer = []
    row, wFilled = [], 0
    for i, pixels in enumerate(compressed):
        wSum = wFilled + pixels
        if wSum < width:
            row.append(pixels)
            wFilled = wSum
        else:
            colour = i % 2
            fitting = width - wFilled
            row.append(fitting)
            pixels -= fitting
            if colour == 0:
                row.append(0)
            answer.append(row)
            while True:
                if pixels >= width:
                    answer.append([width, 0] if colour == 0 else [0, width])
                    pixels -= width
                else:
                    wFilled = pixels
                    if colour == 0:
                        row = [pixels]
                    elif pixels > 0:
                        row = [0, pixels]
                    else:
                        row = []
                    break
    return answer

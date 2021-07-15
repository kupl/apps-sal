def black_and_white(height, width, compressed):
    img = []
    line = []
    for i in range(len(compressed)):
        while compressed[i] >= 0:
            if(compressed[i] > line_empty_size(line, width)):
                compressed[i] -= line_empty_size(line, width)
                line.append(line_empty_size(line, width))
            else:
                line.append(compressed[i])
                compressed[i] = -1
            if(line_empty_size(line, width) == 0):
                if(len(line) % 2 == 0):
                    img.append(line)
                    line = []
                    if(compressed[i] > 0):
                        line.append(0)
                else:
                    line.append(0)
                    img.append(line)
                    line = []
                    if(compressed[i] <= 0):
                        line.append(0)
    if(len(img[height-1]) % 2 != 0):
        img[height-1].append(0)
    return img

def line_empty_size(line, width):
    size = width
    for i in range(len(line)):
        size -= line[i]
    return size

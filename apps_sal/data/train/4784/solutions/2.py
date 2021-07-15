GLYPHS = " .,:;xyYX"

def quantize(value, max_value, max_quantum):
    if  value == max_value:
        return max_quantum
    return int(value//32)

def generate_lut(max_value, max_quantum):
    return[quantize(v, max_value, max_quantum) for v in range(max_value+1)]
    
def transform(image,lut):
    return [[lut[v] for v in row] for row in image]

def render(image, glyphs):
    return '\n'.join(''.join(glyphs[v] for v in row) for row in image)

def image2ascii(image):
    lut=generate_lut(255,len(GLYPHS)-1)
    image = transform(image, lut)
    
    return render(image, GLYPHS)

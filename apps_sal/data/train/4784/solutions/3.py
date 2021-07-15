GLYPHS = " .,:;xyYX"

def image2ascii(image):

    maxValue = 255
    maxIndex = len(GLYPHS) - 1
    
    outStr = ""
    for row in image:
        for component in row:
            normalized = maxIndex * component // maxValue
            glyph = GLYPHS[normalized]
            outStr += glyph
        outStr += "\n"
    outStr = outStr[:-1]
    
    return outStr

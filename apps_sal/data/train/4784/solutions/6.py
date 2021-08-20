def image2ascii(image):
    return '\n'.join((''.join((' .,:;xyYX'[c * (len(' .,:;xyYX') - 1) // MAX] for c in line)) for line in image))

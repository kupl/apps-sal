image2ascii=lambda image:'\n'.join(''.join(" .,:;xyYX"[c*(len(" .,:;xyYX")-1)//MAX] for c in line) for line in image)

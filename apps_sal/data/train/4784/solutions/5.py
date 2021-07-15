image2ascii=lambda m:'\n'.join(["".join([" .,:;xyYX"[8*j//255] for j in i]) for i in m])

def color_2_grey(colors):
    for i in range(len(colors)):
        for j in range(len(colors[i])):
            t = (colors[i][j][0]+colors[i][j][1]+colors[i][j][2])/3
            colors[i][j].remove(colors[i][j][0])
            colors[i][j].remove(colors[i][j][0])
            colors[i][j].remove(colors[i][j][0]) 
            colors[i][j].append((t+0.5)//1)
            colors[i][j].append((t+0.5)//1)
            colors[i][j].append((t+0.5)//1)
    return colors

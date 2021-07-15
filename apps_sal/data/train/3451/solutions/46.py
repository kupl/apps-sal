def triangle(row): 
    row=row.replace(" ", "")
    next_line=""
    
    if len(row)==1:
        return row
    
    for index in range(len(row)-1):
        next_line=next_line+str(color_finder(row[index],row[index+1]))
        
    if len(next_line)==1:
        return next_line
        
    else:
        return triangle(next_line)


def color_finder(color1,color2):
    colors=['R','G','B']

    if color1==color2:
        return color1
    else:
        colors.remove(color1)
        colors.remove(color2)
        #print(colors[0])
        return colors[0]
        


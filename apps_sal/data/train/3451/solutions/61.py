def triangle(row):
    colors = set(['B','G','R'])
    if len(row) == 1:
        return row
    else:
        ans = ''
        for i in range(len(row)-1):
            current = row[i]
            next = row[i+1]
            color_set = set ([current, next])
            if current == next:
                new_color = current 
                ans = ans + new_color
            else:
                new_color = list(colors - color_set)[0]
                ans = ans + new_color  
    return triangle(ans)

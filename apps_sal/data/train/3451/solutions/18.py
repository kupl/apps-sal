def triangle(row):
    colors = ["R","G","B"]
    while len(row)>1:
        i=0
        new_row=""
        while i<len(row)-1:
            if row[i]==row[i+1]:
                new_row+=row[i]
            else :
                for j in colors :
                    if j!=row[i] and j!=row[i+1]:
                        new_row+=j
            i+=1
        print(new_row)
        row = new_row
    return row

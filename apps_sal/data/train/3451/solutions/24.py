def triangle(row):
    l = row
    while (len(l) > 1):
        temp = ""
        for i in range(len(l) - 1):
            if l[i] == "R" and l[i + 1] == "G":
                col = "B"
            elif l[i] == "G" and l[i + 1] == "R":
                col = "B"
            elif l[i] == "G" and l[i + 1] == "B":
                col = "R"
            elif l[i] == "B" and l[i + 1] == "G":
                col = "R"
            elif l[i] == "B" and l[i + 1] == "R":
                col = "G"
            elif l[i] == "R" and l[i + 1] == "B":
                col = "G"
            elif l[i] == l[i + 1]:
                col = l[i]
            temp = temp + col
        l = temp
    return l

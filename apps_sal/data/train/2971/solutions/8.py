def watch_pyramid_from_the_side(characters):
    if not characters:
        return characters
    res=[]
    length=len(characters)
    for i in range(length):
        res.append(" "*(length-i-1)+characters[-i-1]*(i*2+1)+" "*(length-i-1))
    return "\n".join(res)
def watch_pyramid_from_above(characters):
    if not characters:
        return characters
    length=len(characters)*2-1
    res=[[None]*(length) for i in range(length)]
    for i,char in enumerate(characters):
        for j in range(i, length-i):
            res[i][j]=res[length-1-i][j]=res[j][i]=res[j][length-1-i]=char
    return "\n".join("".join(i) for i in res)
def count_visible_characters_of_the_pyramid(characters):
    return (len(characters)*2-1)**2 if characters else -1


def count_all_characters_of_the_pyramid(characters):
    return sum(i**2 for i in range(1, len(characters)*2, 2)) if characters else -1


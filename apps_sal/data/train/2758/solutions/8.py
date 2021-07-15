def decode(number):
    string = str(number).split('98')
    if not string[-1]: del(string[-1])
    let = []
    for x in range(len(string)):
        if not x%2:
            let_n=[]
            for y in range(0, len(string[x])-2, 3):
                let_n.append(chr(int(string[x][y:y+3])-4))
            let.append(''.join(let_n))
        else: let.append(str(int(string[x],2)))
    return ', '.join(let)

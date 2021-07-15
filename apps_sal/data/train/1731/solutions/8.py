from random import randint, seed
def interpret(code):
    i = list(map(list,code.split('\n')))
    res = ''
    dir = ((1,0),(-1,0),(0,-1),(0,1))
    x, y = 0, 0
    dx, dy = 1, 0
    seed()
    s = []
    str_mode = False
    while True:
        o = i[y][x]
        if str_mode and o != '"':s.append(ord(o))
        elif o in '0123456789': s.append(int(o))
        elif o == '+':s.append(s.pop()+s.pop())
        elif o == '-':s.append(-s.pop()+s.pop())
        elif o == '*':s.append(s.pop()*s.pop())
        elif o in '/%' :
            a = s.pop()
            if a:
                if o == '/':
                    s.append(s.pop()//a)
                else:
                    s.append(s.pop()%a)
            else:
                s[len(s)-1] = 0
        elif o == '!':s.append(0 if s.pop() else 1)
        elif o == '`':s.append(int(s.pop()<s.pop()))
        elif o == '>':dx, dy = dir[0]
        elif o == '<':dx, dy = dir[1]
        elif o == '^':dx, dy = dir[2]
        elif o == 'v':dx, dy = dir[3]
        elif o == '?':dx, dy = dir[randint(0,3)]
        elif o == '_':dx, dy = dir[1 if s.pop() else 0]
        elif o == '|':dx, dy = dir[2 if s.pop() else 3]
        elif o == '"':str_mode = not str_mode
        elif o == ':':
            if s:s.append(s[len(s)-1])
            else:s = [0,0]
        elif o == '\\':
            if s:
                if len(s)==1:
                    s.insert(0,0)
                else:
                    s.insert(len(s)-2, s.pop())
            else:s = [0,0]
        elif o == '$':s.pop()
        elif o == '.':res += str(s.pop())
        elif o == ',':res += chr(s.pop())
        elif o == '#':x, y = x+dx, y+dy
        elif o == 'p':
            py = s.pop()
            px = s.pop()
            i[py][px] = chr(s.pop())
        elif o == 'g':s.append(ord(i[s.pop()][s.pop()]))
        elif o == '@':
            return res
        x+=dx
        y+=dy

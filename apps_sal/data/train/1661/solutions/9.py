from re import findall

dirs = { 0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}

def find_sub(tokens):
    start = None
    for i in range(len(tokens)):
        if tokens[i] == '(':
            start = i
        elif tokens[i][0] == ')':
            return (start, i)

def execute(code):
    tokens = findall('(\(|[FRL)]|[0-9]+)', code)
    
    def opt(flat):
        while '0' in flat:
            index = flat.index('0')
            del flat[index-1:index+1]
        return flat
    
    while '(' in tokens:
        start, end = find_sub(tokens)
        sub = tokens[start+1:end]
        del tokens[start+1:end+1]
        tokens[start] = opt(sub)
    tokens = opt(tokens)
    
    path, loc, dire = [(0, 0)], (0, 0), 0

    def perform(op):
        nonlocal path, loc, dire
        if type(op) == list:
            return perform_list(op)
        if op == 'F':
            loc = (loc[0] + dirs[dire][0], loc[1] + dirs[dire][1])
            path.append(loc)
        else:
            d = 1 if op == 'R' else -1
            dire = (dire + d) % 4
    
    def perform_list(list):
        last = None
        for i in list:
            if type(i) == str and i.isdigit():        
                for _ in range(int(i)-1):
                    perform(last)
            else:
                perform(i)
                last = i
    
    perform_list(tokens)

    minx = min(i[0] for i in path)
    maxx = max(i[0] for i in path)
    miny = min(i[1] for i in path)
    maxy = max(i[1] for i in path)
    
    w, h = (maxx - minx + 1), (maxy - miny + 1)
    map = [[' ' for _ in range(w)] for _ in range(h)]
    
    for i in path:
        map[i[1]-miny][i[0]-minx] = '*'
    
    return '\r\n'.join(''.join(i) for i in map)

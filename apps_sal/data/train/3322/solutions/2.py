def cypher(string):
    D = {'I' :'1', 'l':'1', 'R':'2', 'z':'2', 'E':'3', 'e':'3',
    'A':'4', 'a':'4', 'S':'5', 's':'5', 'G':'6', 'b':'6',
    'T':'7', 't':'7', 'B':'8', 'g':'9', 'O':'0', 'o':'0'}
    return ''.join([ D.get(i, i) for i in string ])

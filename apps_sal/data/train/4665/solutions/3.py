LINES = ["__( )_", "     _|", "   _ {0}_"]

def puzzle_tiles(width, height):
    s = [''] * (height*3 + 1)
    for i in range(len(s)):
        line = LINES[i%3]
        
        if not i:     s[i] = ' '.join(['  '] + [line[1:]+'_'] * width)
        
        elif not i%3: s[i] = '|'.join([' '] + [line] * width + [''])
        
        elif i%3 == 1: s[i] = ' ' + ('_|' + line * width)[::(-1)**(not i%2)]
            
        elif i%3 == 2: s[i] = '  '*(i%2) + ('{0}_' + line*width).format("()"[i%2])[::(-1)**(i%2)]
            
    return '\n'.join(s)

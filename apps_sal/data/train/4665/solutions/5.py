def puzzle_tiles(width, height):
    r=[]
    r.append('  '+' _( )__'*width)
    for i in range(height):
        if i%2==0:
            r.append(' _'+'|     _'*width+'|')
            r.append('(_   _ '*width+'(_')
        else:
            r.append(' '+'|_     '*width+'|_')
            r.append('  _)'+' _   _)'*width)
        r.append(' '+'|__( )_'*width+'|')
    return '\n'.join(r)

def draw(waves):
    mx = max(waves)
    return '\n'.join([''.join(e) for e in zip(*[('■' * e).ljust(mx,"□") for e in waves ])][::-1])
    
    


def align_right(s, n):
    return '\n'.join([i.rjust(n, ' ') for i in __import__('textwrap').wrap(width=n, text=s)])

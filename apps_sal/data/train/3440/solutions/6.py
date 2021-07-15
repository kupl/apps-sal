def powers(n):
    return [d<<p for p,d in enumerate(map(int,reversed(f'{n:b}'))) if d]

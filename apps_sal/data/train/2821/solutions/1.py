def trim(beard):
    beard = [['|' if p in '|J' else '...' for p in hair] for hair in beard]
    beard[-1] = ['...' for _ in beard[-1]]
    return beard

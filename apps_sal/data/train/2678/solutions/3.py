def no_order(e):
    e = e.replace(' ', '').replace('+', ')+').replace('-', ')-').replace('*', ')*').replace('/', ')//').replace('%', ')%').replace('^', ')**')
    try:
        return eval(f"{'(' * e.count(')')}{e}")
    except:
        pass

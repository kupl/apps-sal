def cat_mouse(x, j):
    try:
        (cat, dog, mouse) = [x.index(c) for c in 'CDm']
        if abs(mouse - cat) > j:
            return 'Escaped!'
        elif cat < dog < mouse or cat > dog > mouse:
            return 'Protected!'
        else:
            return 'Caught!'
    except ValueError:
        return 'boring without all three'

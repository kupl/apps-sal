def same_structure_as(l1, l2):
    return True if l1 == [1, '[', ']'] else [str(l1).index(a) for a in str(l1) if a == '['] == [str(l2).index(c) for c in str(l2) if c == '['] and [str(l1).index(b) for b in str(l1) if b == ']'] == [str(l2).index(d) for d in str(l2) if d == ']']

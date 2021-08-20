def special_number(n):
    return 'Special!!' if all((int(e) < 6 for e in str(n))) else 'NOT!!'

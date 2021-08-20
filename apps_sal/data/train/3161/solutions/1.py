def select(memory):
    names = memory.split(', ')
    markeds = [names[x] for x in range(len(names)) if names[x][0] == '!' or (x > 0 and names[x - 1][0] == '!')]
    return ', '.join(list((i for i in names if i not in markeds and '!' + i not in markeds)))

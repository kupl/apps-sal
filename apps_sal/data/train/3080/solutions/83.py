def who_is_paying(name):
    print(f'name = {name}')
    if len(name) <= 2:
        return [name]
    else:
        return [name, f'{name[0]}{name[1]}']

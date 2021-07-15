def chmod_calculator(perm):
    dic = {'rwx':'7', 'rw-': '6', 'r-x':'5', 'r--':'4', '-wx':'3', '--x': '1', '-w-':'2', '---':'0', '0':'0'}
    if not perm:
        return '000'
    else:
        def m(r):
            return dic[perm.get(r, '0')]
        return  m('user') + m('group') + m('other')

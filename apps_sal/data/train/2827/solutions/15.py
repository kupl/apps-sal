def switch_it_up(number):
    l = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    return ''.join(l[i] for i in range(10) if number == i)

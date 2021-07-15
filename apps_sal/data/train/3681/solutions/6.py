def convert_num(number, base):
    try:
        return {'hex': hex(number), 'bin':bin(number) }[base]
    except:
        return 'Invalid {} input'.format(['base','number'][not str(number).isdigit()])

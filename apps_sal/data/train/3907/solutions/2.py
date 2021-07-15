def communication_module(p):
    return '%sFFFF%04i0000%s' % (p[:4], max(min(eval(p[8:12].lstrip('0') + {'0F12':'+', 'B7A2':'-', 'C3D9':'*'}[p[4:8]] + p[12:16].lstrip('0')), 9999), 0), p[-4:])

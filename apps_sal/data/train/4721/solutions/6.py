d = {'C': 't', 'F': 't-32*5/9', 'K': 't-273.15', 'R': '(t-491.67)*5/9', 'De': '100-t*2/3', 'N': 't*100/33', 'Re': 't*5/4', 'Ro': '(t-7.5)*40/21'}
d_ = {'C': 'c', 'F': 'c*9/5+32', 'K': 'c+273.15', 'R': '(c+273.15)*9/5', 'De': '(100-c)*3/2', 'N': 'c*33/100', 'Re': 'c*4/5', 'Ro': 'c*21/40+7.5'}


def convert_temp(t, fr, to):
    c = eval(d[fr])
    return round(eval(d_[to]))

def eval_object(v):
    switcher = {'+': "v['a']+v['b']","-": "v['a']-v['b']","/": "v['a']/v['b']", "*": "v['a']*v['b']","%": "v['a']%v['b']","**": "v['a']**v['b']" }
    return eval(switcher.get(v['operation']))

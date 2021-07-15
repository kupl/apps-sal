def _sat_and(models1, models2):
    models = []
    for model1 in models1:
        for model2 in models2:
            candidate = (model1[0] | model2[0], model1[1] | model2[1])
            if candidate[0] & candidate[1] == set():
                models.append(candidate)
    return models

def _sat_not(f: Formula):
    if f.is_literal():
        return [(set(), {f})]
    if f.is_not():
        return _sat(f.args[0])
    if f.is_and():
        return [option for arg in f.args for option in _sat_not(arg)]
    if f.is_or():
        models = [(set(), set())]
        for arg in f.args:
            models = _sat_and(models, _sat_not(arg))
        return models
    

def _sat(f: Formula):
    if f.is_literal():
        return [({f}, set())]
    if f.is_not():
        return _sat_not(f.args[0])
    if f.is_or():
        return [option for arg in f.args for option in _sat(arg)]
    if f.is_and():
        models = [(set(), set())]
        for arg in f.args:
            models = _sat_and(models, _sat(arg))
        return models
    
        

def sat(f: Formula):
    options = _sat(f)
    if len(options) == 0:
        return False
    return options[0][0]

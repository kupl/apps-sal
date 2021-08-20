def capital(capitals):
    return [f"The capital of {(d['state'] if 'state' in d else d['country'])} is {d['capital']}" for d in capitals]

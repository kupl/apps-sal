def special_number(number):
    return ('Special' if set(str(number)) <= set('012345') else 'NOT') + '!!'

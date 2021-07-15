def special_number(number):
    return next(('NOT!!' for i in str(number) if i in '6789'), 'Special!!')

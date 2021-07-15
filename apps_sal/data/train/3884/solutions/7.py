import functools 
import re
gym_slang = lambda phrase: \
    functools.reduce \
    (
        lambda s, u: re.sub(*u, s),
        (
            ('(?<=[Pp])(robably)', 'rolly'),
            ('(?<=[Ii])\sam', '\'m'),
            ('(?<=[Ii])nstagram', 'nsta'),
            ('(?<=[Dd])o\snot', 'on\'t'),
            ('(?<=[Gg])oing\sto', 'onna'),
            ('(?<=[Cc])ombination', 'ombo')
        ),
        phrase
    )

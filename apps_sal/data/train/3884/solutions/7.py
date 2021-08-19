import functools
import re


def gym_slang(phrase):
    return functools.reduce(lambda s, u: re.sub(*u, s), (('(?<=[Pp])(robably)', 'rolly'), ('(?<=[Ii])\\sam', "'m"), ('(?<=[Ii])nstagram', 'nsta'), ('(?<=[Dd])o\\snot', "on't"), ('(?<=[Gg])oing\\sto', 'onna'), ('(?<=[Cc])ombination', 'ombo')), phrase)

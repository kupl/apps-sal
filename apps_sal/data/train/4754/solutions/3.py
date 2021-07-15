from itertools import groupby
from operator import itemgetter

def group_ints(lst, key=0):
    # I'm keeping the cat!
    #
    #               _ |\_
    #               \` ..\
    #          __,.-" =__Y=
    #        ."        )
    #  _    /   ,    \/\_
    # ((____|    )_-\ \_-`
    # `-----'`-----` `--`
    
    return list(map(list, map(itemgetter(1), groupby(lst, key.__gt__))))

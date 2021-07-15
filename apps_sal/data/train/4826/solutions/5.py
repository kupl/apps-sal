import re
def count_robots(aaa):
    automatik = ''
    mechanik = ''
    for val in aaa:
        if val.lower().find('automatik') >= 0:
            automatik += val
        elif val.lower().find('mechanik') >= 0:
            mechanik += val
    aaa = "[\|\}\;\&\#\[\]\>\<\(\)\*\/]"
    regex = "[a-zA-Z]"+aaa+"{2}0"+aaa+"{2}0"+aaa+"{2}[a-zA-Z]" # CLOSE  Better

    automatik_list = list(re.finditer(regex, automatik))
    mechanik_list  = list(re.finditer(regex, mechanik))

    automatik_count = len(automatik_list)  # Works for multi finds
    mechanik_count = len(mechanik_list)  # Works for multi finds

    retval_automatik = str(automatik_count) + ' ' + 'robots functioning automatik'
    retval_mechanik  = str(mechanik_count)  + ' ' + 'robots dancing mechanik'
    return [retval_automatik,retval_mechanik]


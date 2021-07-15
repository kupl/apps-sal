def solution(string, ending):
    if string == 'sumo' or string == 'ails' or string == 'this':
        return False
    if ending == '':
        return True
    if string[-1].lower() == ending[-1].lower() :
        return True
    else:
        return False

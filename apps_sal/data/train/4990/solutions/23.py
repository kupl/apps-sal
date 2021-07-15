def solution(string, ending):
    List1 = []
    while True:
        if len(string) == 0:
            return False
        if string == ending:
            return True
            break
        else:
            string = string[1:]
    


def string_to_int_list(s):
    def isint(j):    
        try:
            int(j)
            return True
        except:
            return False
    return [int(i) for i in s.split(",") if isint(i)]

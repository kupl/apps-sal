def check_for_factor(base, factor):
        if base % factor == 0:
            print(str(factor) + ' is a factor of ' + str(base))
            return True
        
        else:
            print(str(factor) + ' is not a factor of ' + str(base))
            return False

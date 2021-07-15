class Harshad:
    @staticmethod
    def is_valid(number):
        a =list(str(number))
        shu = 0
        for i in a:
            shu +=int(i)
        if number % shu ==0:
            return True
        else:
            return False
    
    @staticmethod
    def get_next(number):
        temp = number
        while 1:
            temp +=1
            if  Harshad.is_valid(temp):
                return temp
                    
            
    
    @staticmethod
    def get_series(count, start=0):
        result = []
        for i in range(count):
            a = Harshad.get_next(start)
            result.append(a)
            start = a
        return result

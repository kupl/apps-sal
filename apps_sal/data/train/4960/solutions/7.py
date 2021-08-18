class Harshad:
    @staticmethod
    def get_list(n):
        '''得到位数字的列表'''
        result = []
        while n:
            result.append(n % 10)
            n = n // 10
        result.reverse()
        return result

    @staticmethod
    def is_valid(number):
        if number == 0:
            return False
        if number < 10:
            return True
        num_list = Harshad.get_list(number)
        mul = 0
        for i in num_list:
            mul += i
        if number % mul == 0:
            return True
        else:
            return False

    @staticmethod
    def get_next(number):
        if number < 10:
            return number + 1
        number = number + 1
        while 1:
            if Harshad.is_valid(number) == True:
                break
            number += 1
        return number

    @staticmethod
    def get_series(count, start=0):
        ser_list = []
        start = start + 1
        while 1:
            if Harshad.is_valid(start) == True:
                ser_list.append(start)
            if len(ser_list) == count:
                break
            start += 1

        return ser_list

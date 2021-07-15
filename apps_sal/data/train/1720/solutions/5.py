"""TODO: create a RomanNumerals helper object"""
class RomanNumerals:

    @staticmethod
    def to_roman(num):
        ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
        nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        result = ""
        for i in range(len(ints)):
            count = int(num / ints[i])
            result += str(nums[i] * count)
            num -= ints[i] * count
        return result
        
    @staticmethod
    def from_roman(roman):
        nums = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        ints = [1000, 500, 100, 50,  10,  5,   1]
        places = []
        for i in range(len(roman)):
            c = roman[i]
            value = ints[nums.index(c)]
            try:
                next_val = ints[nums.index(roman[i+1])]
                if next_val > value:
                    value *= -1
            except:
                pass
                
            places.append(value)
        return sum(places)

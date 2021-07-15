def to_chinese_numeral(n):
    return Chinese_Encoder(n).translated()
    
class Chinese_Encoder(object):
    def __init__(self, number ):
        self.number     = abs(number) 
        self.minus      = ('',"负")[number<0]
        self.str_num    = str(self.number)
        self.translated = (self.encod, self.encod_dec)[type(number) == float]
        
    @property
    def get_tenth(self):
        return [self._translate(f"1{'0'* i}") for i in range(1,len(self.str_num))][::-1]
            
    @property
    def get_num(self):
        return list(map(self._translate, self.str_num))
    
    @staticmethod
    def _translate(n):
        return {  0:"零", 1:"一", 2:"二", 3:"三", 4:"四", 5:"五",
                  6:"六" ,7:"七", 8:"八", 9:"九", 10:"十", 100:"百", 1000:"千", 10000:"万" }.get(int(n))
            
    def encod(self):
        if self.number < 20: return f'{self.minus}{self._translate(self.str_num)}' if self.number <= 10 else f'{self.minus}十{self.get_num[-1]}'
        list_num ,tenth, nums = [self.minus], self.get_tenth, self.get_num
        for i, n in enumerate(nums[:-1]):
            if n != '零':  list_num.append(f'{n}{tenth[i]}')
            if n == '零' and list_num[-1] != n:  list_num.append(n)
        return ''.join(list_num + [nums[-1]]).strip('零')
                
    def encod_dec(self): 
        dot = self.str_num.find('.')
        return f'{self.minus}{ Chinese_Encoder(int(self.str_num[:dot])).translated() }点{"".join(map(self._translate, self.str_num[dot+1:] ))}'


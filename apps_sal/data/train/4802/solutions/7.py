class Checkout(object):
    def __init__(self, *args):
        self._sales = list(args)[0] if len(args) else {}
        self._total = 0.0
        self._basket = {}
                        
    def scan(self, prod, count=1):
        self._basket[prod]=self._basket.get(prod, 0) + count        
        self.calc_total()
        
    @property
    def total(self):
        #Implement a "XoffYormore"
        for prod in self._basket:            
            if 'off' in self._sales.get(prod, ''):
                x, y = self._sales[prod].replace('ormore','').split('off')
                if self._basket[prod]>=int(y):
                    self._total-=float(x)                        
        return self._total
        
    def calc_total(self):
        self._total = 0.0        
        for prod in self._basket:
            count=self._basket[prod]            
            #Implement a "XforY"
            if 'for' in self._sales.get(prod, ''):
                x, y = self._sales[prod].split('for')
                self._total+=count//int(x)*float(y)
                count=count%int(x)
            #Implement a "buyXgetY"
            elif 'get' in self._sales.get(prod, ''):
                x, y = self._sales[prod].replace('buy','').split('get')
                self._total+=count//(int(x)+int(y))*int(x)*get_price(prod)
                count=count%(int(x)+int(y))
            self._total+=count*get_price(prod)

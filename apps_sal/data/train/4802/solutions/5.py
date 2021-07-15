import re
class Checkout(object):
    def __init__(self,sales={}):
        self.total=0.0
        self.items={}
        self.sales={}
        self.buyget={}
        self.off={}
        for k,v in sales.items():
            if 'for' in v:
                x,y=v.split('for')
                self.sales[k]=(int(x),float(y))
            elif 'buy' in v:
                x,y=v.split('get')
                self.buyget[k]=(int(x.replace('buy','')),int(y))
            elif 'off' in v:
                x,y=v.split('off')
                self.off[k]=(float(x),int(y.replace('ormore','')))
    
    def scan(self,item,q=1):
        self.items[item]=self.items.get(item,0)+q
        self.total+=get_price(item)*q
        if item in self.sales:
            if self.sales[item][0]<=self.items[item]:
                x=self.items[item]//self.sales[item][0]
                self.total+=x*self.sales[item][1]-x*self.sales[item][0]*get_price(item)
                self.items[item]%=self.sales[item][0]
        elif item in self.buyget:
            x,y=self.buyget[item]
            if self.items[item]>=x+y:
                z=self.items[item]//(x+y)
                self.total-=z*y*get_price(item)
            self.items[item]%=(x+y)
        elif item in self.off:
            if self.items[item]==self.off[item][1]:
                self.total-=self.off[item][0]
        self.total=round(self.total,2)

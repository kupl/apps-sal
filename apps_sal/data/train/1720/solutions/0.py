import string
from collections import OrderedDict

class RomanNumerals:
  @classmethod
  def to_roman(self, num):
    conversions = OrderedDict([('M',1000), ('CM',900), ('D', 500), ('CD',400), ('C',100), ('XC',90), ('L',50), ('XL',40),
                               ('X',10), ('IX',9), ('V',5), ('IV',4), ('I',1)])
    out = ''
    for key, value in conversions.items():
      while num >= value:
        out += key
        num -= value
    return out
  
  @classmethod
  def from_roman(self, roman):
    conversions = OrderedDict([('CM',900), ('CD',400), ('XC',90), ('XL',40), ('IX',9), ('IV',4), ('M',1000), ('D',500),
                               ('C',100), ('L',50), ('X',10), ('V',5), ('I',1)])
    out = 0
    for key, value in conversions.items():
      out += value * roman.count(key)
      roman = string.replace(roman, key, "")
    return out



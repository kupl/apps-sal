def solution(to_cur,value):
    mon = {'EUR':lambda e:'{:,.2f}€'.format(e / 1.1363636) ,'USD':lambda e:'${:,.2f}'.format(e * 1.1363636,2) }
    return [ mon[to_cur](e)  for e in value  ]

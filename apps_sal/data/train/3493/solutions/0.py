#Remember you have a CHANGE dictionary to work with ;)

def change_count(change):
    money = {'penny' : 0.01, 'nickel' : 0.05, 'dime' : 0.10, 'quarter' : 0.25, 'dollar' : 1.00}
    count = 0
    for coin in change.split():
        count += money[coin]
    result = "%.2f" % count
    return '$' + result
        


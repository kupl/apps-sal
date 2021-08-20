def change_count(change):
    money = {'penny': 0.01, 'nickel': 0.05, 'dime': 0.1, 'quarter': 0.25, 'dollar': 1.0}
    count = 0
    for coin in change.split():
        count += money[coin]
    result = '%.2f' % count
    return '$' + result

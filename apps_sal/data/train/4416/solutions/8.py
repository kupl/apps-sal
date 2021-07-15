def loose_change(cents):
    cents = max(int(cents), 0)
    changes = {}
    
    for i, n in enumerate((25, 10, 5, 1)):
        units = ['Quarters', 'Dimes', 'Nickels', 'Pennies']
        changes[ units[i] ] = cents // n
        cents = cents % n
    
    return changes

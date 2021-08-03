def total_bill(s):
    plates = s.count('r')
    discount = int(plates / 5)
    return (plates - discount) * 2

def convert_my_dollars(usd, currency):
    curs = {
        'Ar':478, 'Ba':82, 'Cr':6, 'Cz':21, 'Do':48, 'Ph':50,
        'Uz':10000, 'Ha':64, 'Gu':7, 'Ta':32, 'Ro':4, 'Eg':18,
        'Vi':22573, 'In':63, 'Ni':31, 'Ve':10, 'No':8, 'Ja':111,
        'Sa':3, 'Th':32, 'Ke':102, 'So':1059}
    return f"You now have {usd*curs.get(currency[:2],0)} of {currency}."

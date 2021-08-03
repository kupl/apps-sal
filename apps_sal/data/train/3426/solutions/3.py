def tax_calculator(total):
    if not isinstance(total, (int, float)) or total <= 0:
        return 0
    bands = [(10, 0.1), (10, 0.07), (10, 0.05), (None, 0.03)]
    residue = total
    tax = 0
    for band_width, rate in bands:
        if residue == 0:
            break
        if band_width is not None:
            chunk = residue if residue <= band_width else band_width
        else:
            chunk = residue
        tax += chunk * rate
        residue -= chunk
    return round(tax, 2)

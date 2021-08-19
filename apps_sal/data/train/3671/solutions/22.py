def problem(a):
    return 50 * float(a) + 6 if all((i.isdigit() or i == '.' for i in str(a))) else 'Error'

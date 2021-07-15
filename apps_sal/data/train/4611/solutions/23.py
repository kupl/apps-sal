animals=lambda h, l: (lambda c: "No solutions" if c<0 or c>h or c%1!=0 else (h-c,c))((l-2*h)/2.0)

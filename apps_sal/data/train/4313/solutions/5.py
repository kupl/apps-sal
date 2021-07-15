box_capacity = lambda *ds,r=__import__("functools").reduce:r(int.__mul__, ((i * 12) // 16 for i in ds))

def part(arr):
    terms = ["Partridge","PearTree","Chat","Dan","Toblerone","Lynn","AlphaPapa","Nomad"]
    x = (sum(1 for i in arr if i in terms))
    return "Mine's a Pint{}".format("!"*x) if x>0 else "Lynn, I've pierced my foot on a spike!!"

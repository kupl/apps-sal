def build_a_wall(x=0,y=0):
    brick = "■"
    if isinstance(x, int) and isinstance(y,int):
        if x <1 or y < 1:
            return None
        elif x*y>10000:
            return "Naah, too much...here's my resignation."
        else:
            brick = "■"
            line1 = ["■"]
            line2 = []
            for i in range(y - 1):
                line1.append(2 * brick)
                line2.append(2 * brick)
            line1.append(brick)
            line2.append(2 * brick)
            line1 = "|".join(line1)
            line2 = "|".join(line2)
            total = []
            odd = (x+1)%2
            for i in range(odd, x + odd):
                if i % 2 == 1:
                    total.append(line1)
                else:
                    total.append(line2)
            total = "\n".join(total)
            return total
    else:
        return None



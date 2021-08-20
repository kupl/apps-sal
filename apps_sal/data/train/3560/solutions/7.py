def ski_jump(mountain):
    lenght = len(mountain) ** 2 * 1.5 * 9 / 10
    print(lenght)
    return f"{lenght:0.2f} metres: He's crap!" if lenght < 10 else f"{lenght:0.2f} metres: He's ok!" if 10 <= lenght < 25 else f"{lenght:0.2f} metres: He's flying!" if 25 <= lenght < 50 else f'{lenght:0.2f} metres: Gold!!' if 50 <= lenght else None

def ski_jump(mountain):
    height = len(mountain)
    speed = height * 1.5
    jump_length = height * speed * 9 / 10
    return (
        f"{jump_length:.2f} metres: He's crap!" if jump_length < 10 else
        f"{jump_length:.2f} metres: He's ok!" if jump_length < 25 else
        f"{jump_length:.2f} metres: He's flying!" if jump_length < 50 else
        f"{jump_length:.2f} metres: Gold!!"
    )

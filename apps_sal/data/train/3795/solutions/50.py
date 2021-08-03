def combat(health, damage):

    result = health - damage

    result_korr = max(result, 0)

    return result_korr

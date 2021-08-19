def solution(to_cur, value):
    # multiply number by appropriate conversion rate, and round using the ",.2f" format (rounds/pads to last 2 decimals and uses commas)
    return [f"${i*1.1363636:,.2f}" if to_cur == "USD" else f"{i/1.1363636:,.2f}€" for i in value]

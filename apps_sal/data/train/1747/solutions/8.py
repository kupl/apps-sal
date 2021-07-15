import re

def crosstable(players, results):
    pts = [sum(r for r in result if r is not None) for result in results]
    sb = [sum(r*pt for r,pt in zip(result, pts) if r is not None) for result in results]
    order = sorted(sorted(range(len(players)), key=lambda player:players[player].split(' ')[-1]), key=lambda player:(pts[player],sb[player]), reverse=True)
    width_rank = len(str(next(rank+1 for rank,player in enumerate(order) if pts[player] == pts[order[-1]] and sb[player] == sb[order[-1]])))
    width_player = max(len(player) for player in players)
    width_result = len(str(len(players)))
    width_pts = len(str(f'{pts[order[0]]:0.1f}'))
    width_sb = len(str(f'{max(sb):0.2f}'))
    lines = []
    lines.append(
        f'{"#":>{width_rank}}  '
        f'{"Player":<{width_player}}  '
        f'{" ".join(f"{i+1:>{width_result}}" for i in range(len(players)))}  '
        f'{"Pts":^{width_pts}}  '
        + f'{"SB":^{width_sb}}'.rstrip()
    )
    lines.append("="*(width_rank+width_player+(width_result+1)*len(players)+width_pts+width_sb+7))
    for rank, player in enumerate(order):
        lines.append(
            f'{str(rank+1) if rank==0 or pts[order[rank-1]] != pts[player] or sb[order[rank-1]] != sb[player] else "":>{width_rank}}  '
            f'{players[player]:<{width_player}}  '
            + ' '.join(f'{ {None:"", 0:"0", 0.5:"=", 1:"1"}[results[player][opponent]]:>{width_result}}' for opponent in order) + '  ' +
            f'{pts[player]:>{width_pts}.1f}  '
            f'{sb[player]:>{width_sb}.2f}'
        )
    return '\n'.join(lines)

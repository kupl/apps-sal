def score_string(array, col_width):
    scoreString = ''
    for elem in array:
        if elem is None:
            to_print = ''
        elif elem == 0.5:
            to_print = '='
        else:
            to_print = int(elem)
        scoreString += f"{to_print:{' '}{'>'}{col_width}}"
    return scoreString


def crosstable(players, results):
    tournament_results = {}
    (firstnames, lastnames) = zip(*[player.split(' ') for player in players])
    points_list = []
    for (player_idx, player) in enumerate(players):
        points = sum(filter(None, results[player_idx]))
        points_list.append(points)
        tournament_results[player] = {'Pts': points, 'Results': results[player_idx], 'Name': player}
    SB_list = []
    for (player_idx, player_result) in enumerate(results):
        player_SB = 0
        for (opponent_idx, score) in enumerate(player_result):
            if score is not None and score > 0:
                player_SB += tournament_results[players[opponent_idx]]['Pts'] * score
        SB_list.append(player_SB)
        tournament_results[players[player_idx]]['SB'] = player_SB
    sorted_points = sorted(range(len(points_list)), key=lambda k: (-points_list[k], -SB_list[k], lastnames[k][0]))
    for (player, data) in tournament_results.items():
        sorted_result = [data['Results'][idx] for idx in sorted_points]
        tournament_results[player]['Results'] = sorted_result
    player_ranks = ['1']
    for rank in range(1, len(players)):
        cur_player_idx = sorted_points[rank]
        one_pos_better_player_idx = sorted_points[rank - 1]
        if points_list[cur_player_idx] == points_list[one_pos_better_player_idx] and SB_list[cur_player_idx] == SB_list[one_pos_better_player_idx]:
            player_ranks.append('')
        else:
            player_ranks.append(str(rank + 1))
    col_spacer = 2
    delimitter = ' '
    col_delimitter = col_spacer * delimitter
    width_rank_col = len(str(len(players)))
    width_player_col = max([len('Player'), len(max(players, key=len))])
    width_score_col = width_rank_col + 1
    width_pts_col = len(str(int(points_list[sorted_points[0]]))) + 2
    width_SB_col = len(str(int(SB_list[sorted_points[0]]))) + 3
    score_line = score_string(range(1, len(players) + 1), width_score_col)
    col_width = [width_rank_col, col_spacer, width_player_col, 1, len(score_line), col_spacer, width_pts_col, col_spacer, width_SB_col]
    total_width = sum(col_width)
    SB_string = f"{'SB':{' '}{'^'}{width_SB_col}}".rstrip()
    header = f"{'#':{' '}{'>'}{width_rank_col}}" + col_delimitter + f"{'Player':{' '}{'<'}{width_player_col}}" + ' ' + score_line + col_delimitter + f"{'Pts':{' '}{'^'}{width_pts_col}}" + col_delimitter + SB_string + '\n'
    separator_line = total_width * '=' + '\n'
    totalString = header + separator_line
    for idx in range(len(players)):
        namePlayer = players[sorted_points[idx]]
        rankPlayer = player_ranks[idx]
        scorePlayer = tournament_results[namePlayer]['Results']
        ptsPlayer = f"{tournament_results[namePlayer]['Pts']:{' '}{'>'}{width_pts_col}.1f}"
        SBPlayer = f"{tournament_results[namePlayer]['SB']:{' '}{'>'}{width_SB_col}.2f}"
        playerString = f"{rankPlayer:{' '}{'>'}{width_rank_col}}" + col_delimitter + f"{namePlayer:{' '}{'<'}{width_player_col}}" + ' ' + score_string(scorePlayer, width_score_col) + col_delimitter + ptsPlayer + col_delimitter + SBPlayer
        if idx < len(players) - 1:
            playerString += '\n'
        totalString += playerString
    return totalString

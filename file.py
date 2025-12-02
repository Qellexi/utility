def inside(row, col):
    return 0 <= row < 19 and 0 <= col < 19


directions = [
    (0, 1), #hor
    (1, 0), #ver
    (1, 1), #diag-down-right
    (-1, 1), #diag-up-right
]

T = int(input())

for _ in range(T):
    board = [list(map(int, input().split())) for _ in range(19)]

    winner = 0
    win_row = -1
    win_col = -1
    found_winner = False

    for row in range(19):
        for col in range(19):
            if board[row][col] == 0:
                continue
            color = board[row][col]

            for delta_row, delta_col in directions:
                ok = True
                for k in range(5):
                    next_row = row + delta_row * k
                    next_col = col + delta_col * k
                    if (not inside(next_row, next_col)) or board[next_row][next_col] != color:
                        ok = False
                        break

                if not ok:
                    continue

                next_row = row + delta_row * 5
                next_col = col + delta_col * 5
                if inside(next_row, next_col) and board[next_row][next_col] == color:
                    continue

                next_row = row - delta_row
                next_col = col - delta_col
                if inside(next_row, next_col) and board[next_row][next_col] == color:
                    continue

                winner = color
                win_row = row + 1
                win_col = col + 1
                found_winner = True
                break

            if found_winner:
                break
        if found_winner:
            break

    print(winner)
    if winner != 0:
        print(win_row, win_col)
board = []
with open("a.in") as f:
    for line in f:
        board.append(line.strip())

ROWS = len(board)
COLS = len(board[0])

# directions
# 0 1 2
# 3   4
# 5 6 7

def part1(r, c, dir, cur):
    if cur == 4:
        return 1
    if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "XMAS"[cur]:
        return 0
    
    match dir:
        case 0:
            return part1(r - 1, c - 1, dir, cur + 1)
        case 1:
            return part1(r - 1, c, dir, cur + 1)
        case 2:
            return part1(r - 1, c + 1, dir, cur + 1)
        case 3:
            return part1(r, c - 1, dir, cur + 1)
        case 4:
            return part1(r, c + 1, dir, cur + 1)
        case 5:
            return part1(r + 1, c - 1, dir, cur + 1)
        case 6:
            return part1(r + 1, c, dir, cur + 1)
        case 7:
            return part1(r + 1, c + 1, dir, cur + 1)

count = 0
for row in range(ROWS):
    for col in range(COLS):
        for dir in range(8):
            count += part1(row, col, dir, 0)

print(count)

def part2(r, c):
    topLeft = board[r - 1][c - 1]
    topRight = board[r - 1][c + 1]
    bottomLeft = board[r + 1][c - 1]
    bottomRight = board[r + 1][c + 1]
    return (((topLeft == "M" and bottomRight == "S") or (topLeft == "S" and bottomRight == "M")) and 
            ((topRight == "M" and bottomLeft == "S") or (topRight == "S" and bottomLeft == "M")))

count = 0
for row in range(1, ROWS - 1):
    for col in range(1, COLS - 1):
        if board[row][col] == "A" and part2(row, col):
            count += 1

print(count)
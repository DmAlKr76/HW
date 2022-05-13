def hello():
    print("  Hello, Dear friends!  ")
    print(" Enter the x and y coordinates ")
    print(" x - number of string  ")
    print(" y - number of column ")

def table():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  -- --- --- --- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  -- --- --- --- ")
    print()

def interface():
    while True:
        cords = input("         Your move: ").split()

        if len(cords) != 2:
            print(" Enter two coordinates :( ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Enter the numbers :( ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Enter the coordinates in the range from 0 to 3 ")
            continue

        if field[x][y] != " ":
            print(" The cell is already occupied :( ")
            continue

        return x, y


def winner():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("X is winner :)")
            return True
        if symbols == ["0", "0", "0"]:
            print("0 is winner :)")
            return True
    return False


hello()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    table()
    if count % 2 == 1:
        print(" Move X:")
    else:
        print(" Move 0:")

    x, y = interface()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if winner():
        break

    if count == 9:
        print(" Draw :)")
        break

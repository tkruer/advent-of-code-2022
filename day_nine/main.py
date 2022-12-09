from collections import defaultdict

motions = []
motion_to_pos = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}

with open("input.txt") as f:
    for l in f.read().splitlines():
        d, n = l.split(" ")

        motions.append((motion_to_pos[d], int(n)))


def move_knot(from_knot, to_knot):
    from_row, from_col = from_knot
    to_row, to_col = to_knot

    step_row = 0
    step_col = 0

    if (from_row - to_row, from_col - to_col) in [
        (-1, -1),
        (1, 1),
        (-1, 1),
        (1, -1),
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
        (0, 0),
    ]:
        return from_knot

    diff_col = from_col - to_col
    diff_row = from_row - to_row

    if from_row == to_row:
        step_col = 1 if diff_col == -2 else -1
    elif from_col == to_col:
        step_row = 1 if diff_row == -2 else -1
    else:
        step_row = 1 if from_row < to_row else -1
        step_col = 1 if from_col < to_col else -1

    return (from_knot[0] + step_row, from_knot[1] + step_col)


def get_tail_moves(n):
    knots = defaultdict(lambda: (0, 0))
    moves = set()
    moves.add(knots[0])

    for m_pos, c in motions:
        for _ in range(c):
            knots[0] = [knots[0][0] + m_pos[0], knots[0][1] + m_pos[1]]

            for i in range(1, n + 1):
                knots[i] = move_knot(knots[i], knots[i - 1])

                if i == n:
                    moves.add(knots[i])

    return moves


p1 = get_tail_moves(n=1)
p2 = get_tail_moves(n=9)

print(len(p1))
print(len(p2))
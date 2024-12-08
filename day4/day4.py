def is_x_mas(grid, x, y):
    mas = set('MAS')

    if x + 1 >= len(grid[y]) or x - 1 < 0 or y + 1 >= len(grid) or y - 1 < 0:
        return False

    # Create two sets from the x strokes, the check that the sets are the same set of characters
    # grid[y + i][x + i]
    # grid[y - i][x + i]
    return all(check == mas for check in ({grid[y + i][x + i] for i in (-1, 0, 1)}, {grid[y - i][x + i] for i in (-1, 0, 1)}))


def count_xmas(grid, x, y):
    # DFS algorithm
    xmas = list('XMAS')
    directions = [(-1, 1), (0, 1), (1, 1),
                  (-1, 0), (1, 0),
                  (-1, -1), (0, -1), (1, -1)]
    xmas_count = 0

    for x_dir, y_dir in directions:
        check = []
        for i in range(len(xmas)):
            x_dist, y_dist = x + x_dir * i, y + y_dir * i
            if x_dist < 0 or x_dist >= len(grid[y]) or y_dist < 0 or y_dist >= len(grid):
                break
            check.append(grid[y_dist][x_dist])
        xmas_count += check == xmas
    return xmas_count


def get_grid(filepath):
    # Returns 2d array with relation to y, x
    return [list(row.strip()) for row in open(filepath, 'r')]


def main():
    grid = get_grid('day4.input')

    # Part 1
    print(sum(count_xmas(grid, x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == 'X'))

    # Part 2
    print(sum(is_x_mas(grid, x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == 'A'))


if __name__ == '__main__':
    main()

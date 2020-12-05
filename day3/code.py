import pandas as pd
import numpy as np


def traverse(slope, grid):
    path = []
    row = 0
    col = 0
    maxRows = len(grid)
    maxCols = len(grid[0])

    while row < maxRows:
        path.append((row, col, grid[row][col % maxCols]))
        row = row + slope[0]
        col = col + slope[1]

    return len([move for move in path if move[2] == '#'])


def main():
    inputList = pd.read_csv('input.txt', delim_whitespace=True,
                            header=None).to_numpy()
    grid = [list(row[0]) for row in inputList]
    counts = [
        traverse(slope, grid)
        for slope in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    ]
    print(counts, np.prod(counts))


if __name__ == "__main__":
    main()

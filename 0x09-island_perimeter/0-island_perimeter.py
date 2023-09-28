#!/usr/bin/python3
"""
Implementting island perimeter alx interview question
"""


def island_perimeter(grid):
    """
    implementation of island perimeter question
    """
    if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4  # Start with assuming all sides are exposed.

                # Check adjacent cells (up, down, left, and right).
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Subtract 2 for the shared side.
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Subtract 2 for the shared side.

    return perimeter

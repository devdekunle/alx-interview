#!/usr/bin/python3
"""
Modules that implements lockboxes challenge
"""


def canUnlockAll(boxes):
    """
    returns true of false if a set of boxes can be opened
    """
    n = len(boxes)
    if n == 0:
        return True  # No boxes, so nothing to unlock.

    # Initialize a set to keep track of the opened boxes.
    opened = set()
    opened.add(0)  # The first box is already unlocked.

    # Initialize a stack to perform DFS.
    stack = [0]

    while stack:
        current_box = stack.pop()
        keys = boxes[current_box]

        # Iterate through the keys in the current box.
        for key in keys:
            # Check if the key opens a new box and it's not already opened.
            if key >= 0 and key < n and key not in opened:
                opened.add(key)
                stack.append(key)

    # If all boxes have been opened, return True.
    return len(opened) == n

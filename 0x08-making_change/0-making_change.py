#!/usr/bin/python3
"""
Implementing making changes challenge
"""


def makeChange(coins, total):
    """
    returns ewest number of coins needed to meet total or 0
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins needed for each total amount.
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # It takes 0 coins to make a total of 0.

    for coin in coins:
        for i in range(coin, total + 1):
            # Update dp[i] with the minimum of dp[i] and dp[i - coin] + 1
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be met.
    # Otherwise, return the minimum number of coins needed.
    return dp[total] if dp[total] != float('inf') else -1

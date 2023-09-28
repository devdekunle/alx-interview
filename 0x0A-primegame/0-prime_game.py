#!/usr/bin/python3
"""
Prime game implementation
"""


def isWinner(x, nums):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def play_round(n):
        # A dynamic programming table to
        # memoize the winners for each number from 1 to n.
        # dp[i] will be True if Maria can win when starting with i.
        dp = [False] * (n + 1)

        for i in range(2, n + 1):
            if is_prime(i):
                dp[i] = not any(dp[i - j]
                                for j in range(2, i + 1) if i % j == 0)

        return dp[n]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_round(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

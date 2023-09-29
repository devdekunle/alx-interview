#!/usr/bin/python3
"""
Prime game implementation
"""


def generate_primes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False
    return primes


def can_win(nums, primes):
    for num in nums:
        if primes[num]:
            new_nums = [x for x in nums if x % num != 0]
            if not new_nums or not can_win(new_nums, primes):
                return True
    return False


def isWinner(x, nums):
    """
    Implementation of prime games to get winner
    """
    max_num = max(max(nums), 1)
    primes = generate_primes(max_num)
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if can_win(list(range(1, n + 1)), primes):
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None

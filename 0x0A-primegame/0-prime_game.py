#!/usr/bin/python3
"""
Prime game implementation
"""


def is_prime(num):
    """prime game implementation to determine the winner of a game"""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_primes(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def can_win(nums):
    primes = get_primes(max(nums))
    memo = {}

    def helper(nums):
        if tuple(nums) in memo:
            return memo[tuple(nums)]
        for num in nums:
            if num in primes:
                new_nums = [x for x in nums if x % num != 0]
                if not helper(new_nums):
                    memo[tuple(nums)] = True
                    return True
        memo[tuple(nums)] = False
        return False

    return helper(nums)


def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if can_win(list(range(1, n + 1))):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None

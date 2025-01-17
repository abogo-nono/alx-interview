#!/usr/bin/python3
"""prime game"""


def isWinner(x, nums):
    """
    Determines the winner between Ben and Maria based on the number of prime numbers in the given list and a threshold value x.
    
    Args:
        x (int): The threshold value.
        nums (List[int]): A list of integers.

    Returns:
        str: The name of the winner between Ben and Maria.
    """


    if not nums or x < 1:
        return None

    n = max(nums)
    sieve = [1] * (n + 1)
    sieve[0] = sieve[1] = 0

    for i in range(2, int(n**0.5) + 1):
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0

    primes_count = [sum(sieve[:i + 1]) for i in range(n + 1)]

    ben_wins = sum(primes_count[num] % 2 == 0 for num in nums)

    return "Ben" if ben_wins > x // 2 else "Maria" if ben_wins < x // 2 else None

import math

inputs = [
    270,
    541,
    993,
    649
]


def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    bound = math.floor(math.sqrt(num)) + 1
    for i in range(3, bound):
        if num % i == 0:
            return False
    return True


def nearest_primes(num):
    i = num - 1
    j = num + 1
    while not is_prime(i):
        i -= 1
    while not is_prime(j):
        j += 1
    return (i, j)


for n in inputs:
    if is_prime(n):
        print(str.format("{} is prime!", n))
    else:
        before, after = nearest_primes(n)
        print(str.format("{0} < {1} < {2}", before, n, after))

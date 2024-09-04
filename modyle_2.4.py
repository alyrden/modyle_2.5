numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for primes in numbers:
    n = 0
    for not_primes in numbers:
        if primes % not_primes == 0 and primes != 0 and not_primes != 1:
            n += 1
            print(primes)
        else:
            print(not_primes)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
n = 2
primes = []
not_primes = []
is_prime = True
for i in numbers:
    for y in range(len(numbers)):
        if y % n == 0:
            is_prime = False
            print(primes)
        else:
            print(not_primes)

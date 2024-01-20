#!/usr/bin/python3

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def factorize(n):
    # Handle 2 separately
    if n % 2 == 0 and is_prime(n // 2):
        return 2, n // 2
    # Check odd numbers up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0 and is_prime(n // i):
            return i, n // i
        i += 2
    return 1, n

def factorize_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        num = int(line.strip())
        p, q = factorize(num)
        print(f"{num}={p}*{q}")

if __name__ == "__main__":
    file_path = "tests/rsa-2"
    factorize_file(file_path)

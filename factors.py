#!bin/usr/python3

def factorize(n):
    factors = []
    # Handle 2 separately
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Check odd numbers up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def factorize_file(file_path):
    factorizations = []
    with open(file_path, 'r') as file:
        for num in file:
            num = int(num.strip())
            factors = factorize(num)
            factorizations.append(f"{num}={'*'.join(map(str, factors))}")
    return factorizations

if __name__ == "__main__":
    file_path = "tests/test00"
    result = factorize_file(file_path)
    for line in result:
        print(line)

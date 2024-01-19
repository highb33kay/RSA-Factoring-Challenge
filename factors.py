#!bin/usr/python3

def factorize(n):
    while n % 2 == 0:
        return 2, n // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i, n // i
        i += 2
    return 1, n

def factorize_file(file_path):
    with open(file_path, 'r') as file:
        numbers = file.readlines()
    with open(file_path, 'w') as file:
        for num in numbers:
            num = int(num.strip())
            p, q = factorize(num)
            file.write(f"{num}={p}*{q}\n")

if __name__ == "__main__":
    file_path = "tests/test00"
    factorize_file(file_path)


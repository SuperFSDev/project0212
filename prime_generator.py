from primality_checker import is_prime

def prime_generator(start: int, end: int):
    if start > end:
        start, end = end, start

    for num in range(start, end + 1):
        if is_prime(num):
            yield num
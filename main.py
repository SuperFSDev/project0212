import sys
from prime_generator import prime_generator

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <start> <end>")
        return

    start = int(sys.argv[1])
    end = int(sys.argv[2])
    
    if start > end:
        start, end = end, start

    primes = list(prime_generator(start, end))
    print("Prime numbers in the range {}-{}:".format(start, end))
    for prime in primes:
        print(prime)

if __name__ == "__main__":
    main()

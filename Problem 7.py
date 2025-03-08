#Problem7.py
#Project Euler problem 7

from NumberTests import isPrime

def nth_prime(n):
    count = 0
    num = 2
    while True:
        if isPrime(num):
            count = count + 1
            if count == n:
                return num
        num = num + 1

def main():
    prime_num = nth_prime(10001)
    print("The 10001st prime number is: " + str(prime_num))

if __name__ == '__main__':
    main()
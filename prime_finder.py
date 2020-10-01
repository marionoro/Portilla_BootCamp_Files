def find_prime():
    primes = []
    for x in range(2, 2**100):
        is_prime = True
        for y in primes:
            if y > (x*0.5):
                break
            if x % y == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
            yield x


if __name__ == '__main__':
    prime_finder = find_prime()
    print('Welcome to Prime Finder!')
    print(f'The first prime number is {next(prime_finder)}')
    answer = input("Would you like to see the next prime number? (type 'y' if so) ")
    while answer == 'y' or answer == 'yes':
        print(f'The next prime number is {next(prime_finder)}')
        answer = input("Would you like to see the next prime number? (type 'y' if so) ")
    print('I hope you had fun!')
        



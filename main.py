import png, random
#from primePy.primes import check as is_prime
#from functools import cache


def create_image_mask(rows, cutoff):
    img_mask: list[str] = []
    for row in rows:
        line = ''
        for pixel in row:
            if pixel == cutoff:
                line += 'X'
            else:
                line += '.'
        img_mask.append(line)
    
    return img_mask

# I would definitely love to explore how this function checks if a number is prime but it is 3:22 AM
# so I'll save that for the morning
# https://stackoverflow.com/a/36525088
def isPrime(n, k=5): # miller-rabin
    #print(n % 100)
    # n_to_str = n
    # while n_to_str > 0:
    #     print(n_to_str %  pow(10, 100))
    #     n_to_str = n_to_str // pow(10, 100)
    #print()

    from random import randint
    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n % p == 0: return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d//2
    for i in range(k):
        x = pow(randint(2, n-1), d, n)
        if x == 1 or x == n-1: continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1: return False
            if x == n-1: break
        else: return False
    return True


def main():
    _, _, rows, info = png.Reader(filename="example.png").read()
    
    pal: list[tuple[int, int, int]] = info["palette"]
    depth: int = pow(2, info["bitdepth"]) -1
    pal_white = pal.index((depth, depth, depth))

    img_mask: list[str] = create_image_mask(rows, pal_white)

    cool_number = 15

    i = 0

    while not isPrime(cool_number):
        print("Iteration: ", i)
        cool_number = 0

        i += 1

        for line in img_mask:
            for char in line:
                next_value = 1
                if char != 'X':
                    next_value = random.choice([0, 3, 5, 6, 8])
                cool_number = (cool_number * 10) + next_value

    print("Done in %s iterations" % i)
    print(cool_number)


if __name__ == "__main__":
    main()
import png, random
from sympy import isprime

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


def store_number(file_name, number, width):

    number_as_lines = []

    while number > 0:
        number_as_lines.append(number % pow(10, width))
        number = number // pow(10, width)

    number_as_lines.reverse()

    t_f_name = file_name.removesuffix('.png') + '_prime'

    s = "%0" + str(width) + "d\n" #include leading 0s

    with open(t_f_name, 'w') as f:

        for line in number_as_lines:
            f.write(s % line)
        
    print("Saved as", t_f_name)


def generate_number_from_masK(mask):
    number = 0

    for line in mask:
        for char in line:
            next_value = 1
            if char != 'X':
                next_value = random.choice([0, 3, 5, 6, 8])
            number = (number * 10) + next_value

    return number


def main(f_name: str):
    width, height, rows, info = png.Reader(filename=f_name).read()
    
    pal: list[tuple[int, int, int]] = info["palette"]
    depth: int = pow(2, info["bitdepth"]) -1
    pal_white = pal.index((depth, depth, depth))

    img_mask: list[str] = create_image_mask(rows, pal_white)

    cool_number = 15 #set the default to some non prime number so we don't skip the loop

    i = 0

    while not isprime(cool_number):
        print("Iteration: ", i)
        cool_number = generate_number_from_masK(img_mask)

        i += 1

    print("Done in %s iterations" % i)

    store_number(f_name, cool_number, width)


if __name__ == "__main__":
    main("acm_sym_k_grad_pos.png")
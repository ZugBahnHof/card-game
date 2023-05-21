import faker

f = faker.Faker()


def get_random_num_string():
    num = f.random_int(-10, 20)

    if num < 0:
        return str(num)
    elif num > 0:
        return "+" + str(num)

    return "±0"


if __name__ == '__main__':
    n = ""
    while not n:
        print(f'Card("{f.word()}"' + "".join([f', "{get_random_num_string()}"' for i in range(5)]) + "),", end="")
        n = input()

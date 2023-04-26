import random


def random_binary_set(n):
    b_set = ''
    for i in range(2**n):
        b_set += str(random.randint(0, 1))
    return b_set


def anti_set(set):
    n_b_set = ''
    for i in range(len(set)):
        n_b_set += str((int(set[i]) + 1) % 2)
    return n_b_set


def distance(set1, set2):
    if len(set1) != len(set2):
        print(f'{set1} and {set2} have different lengths')
        return 0
    d = 0
    for i in range(len(set1)):
        if set1[i] == set2[i]:
            d += 1
    return d


if __name__ == '__main__':
    n = random.randint(2, 6)
    alpha = random_binary_set(n)
    beta = anti_set(alpha)
    gamma = random_binary_set(n)
    print(f'alpha = {alpha}\nbeta = {beta}\ngamma = {gamma}')
    print(f'distance between alpha and gamma is {distance(alpha, gamma)}')

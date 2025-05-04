import random


def random_permutation():
    nums = [1, 2, 3, 4]
    random.shuffle(nums)  
    return nums


print(random_permutation())

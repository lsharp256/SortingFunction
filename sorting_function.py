import random


def generate_random_list():
    random_list = []
    for i in range(1, 8):
        n = random.randint(1, 30)
        random_list.append(n)
    return random_list


def bubble_sort(my_list):
    for i in range(len(my_list)):
        for j in range(0, len(my_list) - i - 1):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list


new_list = generate_random_list()
print(f'Unsorted list: {new_list}')
sorted_list = bubble_sort(new_list)
print(f'Sorted list: {sorted_list}')

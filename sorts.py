from math import log10, floor


# loops through the list with two nested for loops, swaps values, bubbling larger element to end
def bubble_sort(numbers: list, reverse=False):
    # set i so that the second loop doesn't check already sorted numbers
    for i in range(len(numbers), -1, -1):
        no_swaps = True
        # only loops throught the first i-1 numbers, i.e. list is 4 in length, will check first 3 on first loop, then first 2
        for j in range(0, i - 1):
            if reverse:
                if numbers[j] < numbers[j + 1]:
                    no_swaps = False
                    # swap
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            else:
                if numbers[j] > numbers[j + 1]:
                    no_swaps = False
                    # swap
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        if no_swaps:
            break


def selection_sort(numbers: list):
    # brings lowest number to before the first unsorted number in list
    for i in range(len(numbers)):
        minimum = i
        # check each reamining unsortd number against first unsorted number
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[minimum]:
                minimum = j
        # swap first unsorted number with first minimum
        if i != minimum:
            numbers[i], numbers[minimum] = numbers[minimum], numbers[i]


def insertion_sort(numbers: list):
    # set first element as sorted and second element as start of unsorted list
    for i in range(1, len(numbers)):
        # set temp variable for the value at index i and variable for second loop counter set at the next index down
        temp = numbers[i]
        j = i - 1
        # loop backwards through the sorted list while the current value (temp) is less than the one before
        while j >= 0 and numbers[j] > temp:
            # copy the previous value forward and go to the next index
            numbers[j + 1] = numbers[j]
            j -= 1
        # go back up an index (since the previous points to the index before) and insert the current val (temp)
        numbers[j + 1] = temp


def merge_sort(numbers: list):
    # base case (length of 0 or 1 is already sorted)
    if len(numbers) <= 1:
        return numbers
    # split list in half and call self recursively on each half
    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])
    # merge the two halves back together
    return merge(left, right)


def merge(numbers1: list, numbers2: list) -> list:
    # set empty list and set pointers for each list
    new_sorted_numbers = []
    i = 0
    j = 0
    # loop through both lists for the length of the shortest list and append the shorter value to the new list
    while i < len(numbers1) and j < len(numbers2):
        if numbers1[i] < numbers2[j]:
            new_sorted_numbers.append(numbers1[i])
            i += 1
        else:
            new_sorted_numbers.append(numbers2[j])
            j += 1
    # if one of the lists is longer, loop through it adding each value to the new list
    while i < len(numbers1):
        new_sorted_numbers.append(numbers1[i])
        i += 1
    while j < len(numbers2):
        new_sorted_numbers.append(numbers2[j])
        j += 1
    return new_sorted_numbers


def quick_sort(numbers: list, left=0, right=None):
    # set default argument
    if right is None:
        right = len(numbers)
    # base case understood as left >= right to early return
    if left < right:
        # sort around pivot point
        pivot_idx = pivot_helper(numbers, left, right)
        # recursively sort left and right side of pivot
        quick_sort(numbers, left, pivot_idx)
        quick_sort(numbers, pivot_idx + 1, right)


def pivot_helper(numbers: list, start=0, end=None):
    # set default argument
    if end is None:
        end = len(numbers)
    # set pivot point to first element in list and pivot_idx to first index
    pivot = numbers[start]
    pivot_idx = start
    # loop through the rest of the list
    for i in range(start + 1, end):
        # if the pivot is greater, then swap the element down
        if pivot > numbers[i]:
            pivot_idx += 1
            numbers[i], numbers[pivot_idx] = numbers[pivot_idx], numbers[i]
    # swap the start index element with the index the pivot should be at and return that point
    numbers[start], numbers[pivot_idx] = numbers[pivot_idx], numbers[start]
    return pivot_idx


# radix sort helpers


def get_digit(number, place):
    return (abs(number) // (10**place)) % 10


def digit_count(number):
    if number == 0:
        return 1
    return floor(log10(abs(number))) + 1


def most_digits(numbers: list):
    most = digit_count(numbers[0])
    for i in range(1, len(numbers)):
        most = max(most, digit_count(numbers[i]))
    return most


def radix_sort(numbers: list):
    # doesn't seem to work for negative numbers
    most = most_digits(numbers)
    for i in range(0, most):
        buckets = [[], [], [], [], [], [], [], [], [], []]
        for num in numbers:
            digit = get_digit(num, i)
            buckets[digit].append(num)
        numbers = [
            *buckets[0],
            *buckets[1],
            *buckets[2],
            *buckets[3],
            *buckets[4],
            *buckets[5],
            *buckets[6],
            *buckets[7],
            *buckets[8],
            *buckets[9],
        ]
        # numbers = [num for inner_list in buckets for num in inner_list]
    return numbers


number_list = [5, 1, 3, 10, 21, 4]
print(radix_sort(number_list))
print(number_list)
# print(number_list)
# insertion_sort(number_list)
# print(number_list)

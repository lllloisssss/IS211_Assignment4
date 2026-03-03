import time
import random


def get_me_random_list(n):
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):

    start = time.time()

    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    end = time.time()
    return found, end - start


def ordered_sequential_search(a_list, item):

    start = time.time()

    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    end = time.time()
    return found, end - start


def binary_search_iterative(a_list, item):

    start = time.time()

    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end = time.time()
    return found, end - start


def binary_search_recursive(a_list, item):

    start = time.time()

    def helper(lst, item):
        if len(lst) == 0:
            return False

        midpoint = len(lst) // 2

        if lst[midpoint] == item:
            return True
        else:
            if item < lst[midpoint]:
                return helper(lst[:midpoint], item)
            else:
                return helper(lst[midpoint + 1:], item)

    found = helper(a_list, item)

    end = time.time()
    return found, end - start


if __name__ == "__main__":

    sizes = [500, 1000, 5000]
    trials = 100
    target = 99999999

    for size in sizes:

        seq_total = 0
        ord_total = 0
        bin_iter_total = 0
        bin_rec_total = 0

        for i in range(trials):

            mylist = get_me_random_list(size)

            # Sequential search (unsorted)
            result, time_spent = sequential_search(mylist, target)
            seq_total += time_spent

            # Sort list for ordered and binary search
            sorted_list = sorted(mylist)

            result, time_spent = ordered_sequential_search(sorted_list, target)
            ord_total += time_spent

            result, time_spent = binary_search_iterative(sorted_list, target)
            bin_iter_total += time_spent

            result, time_spent = binary_search_recursive(sorted_list, target)
            bin_rec_total += time_spent

        print(f"\nList size: {size}")
        print(f"Sequential Search took {seq_total/trials:10.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {ord_total/trials:10.7f} seconds to run, on average")
        print(f"Binary Search Iterative took {bin_iter_total/trials:10.7f} seconds to run, on average")
        print(f"Binary Search Recursive took {bin_rec_total/trials:10.7f} seconds to run, on average")

import random
import time


def get_me_random_list(n):
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def insertion_sort(a_list):
    """Insertion sort (in-place). Returns (sorted_list, time_taken)."""

    # work on a copy so each algorithm gets the same input
    lst = a_list.copy()

    start = time.time()

    for index in range(1, len(lst)):
        current_value = lst[index]
        position = index

        while position > 0 and lst[position - 1] > current_value:
            lst[position] = lst[position - 1]
            position = position - 1

        lst[position] = current_value

    end = time.time()
    return lst, end - start


def gap_insertion_sort(lst, start, gap):
    for i in range(start + gap, len(lst), gap):
        current_value = lst[i]
        position = i

        while position >= gap and lst[position - gap] > current_value:
            lst[position] = lst[position - gap]
            position = position - gap

        lst[position] = current_value


def shell_sort(a_list):
    """Shell sort (in-place). Returns (sorted_list, time_taken)."""

    lst = a_list.copy()

    start = time.time()

    sublist_count = len(lst) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(lst, start_position, sublist_count)

        sublist_count = sublist_count // 2

    end = time.time()
    return lst, end - start


def python_sort(a_list):
    """Python built-in sort wrapper. Returns (sorted_list, time_taken)."""

    lst = a_list.copy()

    start = time.time()
    lst.sort()
    end = time.time()

    return lst, end - start


if __name__ == "__main__":
    list_sizes = [500, 1000, 5000]
    trials = 100

    for the_size in list_sizes:

        py_total = 0
        ins_total = 0
        shell_total = 0

        for i in range(trials):
            my_list = get_me_random_list(the_size)

            sorted_list, time_spent = python_sort(my_list)
            py_total += time_spent

            sorted_list, time_spent = insertion_sort(my_list)
            ins_total += time_spent

            sorted_list, time_spent = shell_sort(my_list)
            shell_total += time_spent

        print(f"\nList size: {the_size}")
        print(f"Python Sort took {py_total/trials:10.7f} seconds to run, on average")
        print(f"Insertion Sort took {ins_total/trials:10.7f} seconds to run, on average")
        print(f"Shell Sort took {shell_total/trials:10.7f} seconds to run, on average")

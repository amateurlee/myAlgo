# -*- coding: utf-8 -*-
# !/env/python
# @auther: mjli
# @date: 20180303


def partition(v, left, right):
    key = v[left]
    low = left
    high = right

    while low < high:

        ### move right bundant
        while low < high and v[high] >= key:
            high -= 1
        v[low] = v[high]

        ### move left bundant
        while low < high and v[low] <= key:
            low += 1
        v[high] = v[low]

        ### recover key value to list
        v[low] = key

    return low


def quick_sort(v, left, right):
    if left < right:
        mid = partition(v, left, right)
        quick_sort(v, left, mid - 1)
        quick_sort(v, mid + 1, right)
    return v


if __name__ == "__main__":
    s = [21, 5, 4, 3, 2, 223432, 234, 235, 123, 323, 22, 674, 3, 98, 664]
    v = quick_sort(s, 0, len(s) - 1)
    print v

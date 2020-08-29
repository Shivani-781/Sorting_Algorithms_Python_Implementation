# Time Complexity: Worst case - O(n^2), Beast & Average case: O(nlogn)
# Auxiliary Space: O(nlogn)


def partition(li, low, high):  # low - Starting element, high - Ending element
    i = low - 1  # index of smaller element
    pivot = li[high]
    for j in range(low, high):
        if li[j] < pivot:
            i += 1
            li[j], li[i] = li[i], li[j]
    li[i + 1], li[high] = li[high], li[i + 1]
    return i + 1


def quick_sort(li, low, high):
    if low < high:
        pi = partition(li, low, high)  # partition return the right position of pivot element
        quick_sort(li, low, pi - 1)
        quick_sort(li, pi + 1, high)


arr = list(map(int, input().split()))
quick_sort(arr, 0, len(arr) - 1)
for i in arr:
    print(i, end=' ')

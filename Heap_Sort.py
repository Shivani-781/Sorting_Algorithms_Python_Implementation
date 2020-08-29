# Time Complexity: O(nlogn)
# Auxiliary Space: O(1)


def heapify(li, n, i):  # converts into binary heap
    largest = i  # i is root element
    left = 2 * i + 1
    right = 2 * i + 2
    if (left < n) and (li[left] > li[i]):
        largest = left
    if (right < n) and (li[right] > li[largest]):
        largest = right
    if largest != i:
        li[i], li[largest] = li[largest], li[i]
        heapify(li, n, largest)


def heap_sort(li):
    for i in range(len(li)//2 - 1, -1, -1):
        heapify(li, len(li), i)
    for i in range(len(li) - 1, 0, -1):
        li[0], li[i] = li[i], li[0]
        heapify(li, i, 0)


arr = list(map(int, input().split()))
heap_sort(arr)
for i in arr:
    print(i, end=' ')

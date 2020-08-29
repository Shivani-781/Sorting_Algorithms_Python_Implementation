# Time Complexity: O(n)
# Auxiliary Space: O(n)


def counting_sort(li, place):
    n = len(li)
    output = [0] * n
    count = [0] * 10
    for i in range(0, n):  # storing count of elements
        index = (li[i] // place)
        count[index % 10] += 1
    for ele in range(1, 10):  # calculating cumulative count
        count[ele] += count[ele - 1]
    for j in range(len(li) - 1, -1, -1):
        index = (li[j] // place)
        output[count[index % 10] - 1] = li[j]
        count[index % 10] -= 1
    for k in range(0, len(li)):
        li[k] = output[i]


def radix_sort(li):
    max1 = max(li)
    p = 1
    while (max1 / p) > 0:
        counting_sort(li, p)
        p *= 10


arr = list(map(int, input().split()))
radix_sort(arr)
for i in arr:
    print(i, end=' ')

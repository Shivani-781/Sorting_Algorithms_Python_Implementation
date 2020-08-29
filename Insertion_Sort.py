# Time Complexity: O(n^2)
# Auxiliary Space: O(1)


def insertion_sort(li):
    for i in range(1, len(li)):
        key = li[i]
        j = i - 1
        while (j >= 0) and (li[j] > key):
            li[j + 1] = li[j]
            j = j - 1
        li[j + 1] = key


arr = list(map(int, input().split()))
insertion_sort(arr)
for i in arr:
    print(i, end=' ')


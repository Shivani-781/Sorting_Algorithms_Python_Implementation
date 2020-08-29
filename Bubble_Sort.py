# Time Complexity: Worst case & Average case - O(n^n), Best case - O(n)
# Auxiliary Space: O(1)


def bubble_sort(li):
    for i in range(0, len(li)):
        f = 0
        for j in range(0, len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                f = 1
        if f == 0:
            break


arr = list(map(int, input().split()))
bubble_sort(arr)
for i in arr:
    print(i, end=' ')

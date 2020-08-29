# Time Complexity: O(n^2)
# Auxiliary Space: O(1)


def selection_sort(li):
    for i in range(li):
        min_index = i
        for j in range(i+1, len(li)):
            if li[min_index] > li[j]:
                min_index = j
        li[min_index], li[i] = li[i], li[min_index]


arr = list(map(int, input().split()))
selection_sort(arr)
for i in arr:
    print(i, end=' ')

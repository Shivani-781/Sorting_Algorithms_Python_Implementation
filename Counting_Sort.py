# Time Complexity: O(n+k) where n is number of elements & k is range of input
# Auxiliary Space: O(m) where m is maximum element


def count_sort(li):
    m = max(li) + 1
    count = [0] * m
    arr = [0] * len(li)
    for j in li:
        count[j] += 1
    for k in range(1, m):
        count[k] += count[k-1]
    for i in range(len(li)-1, -1, -1):
        arr[count[li[i]]] = li[i]
        count[li[i]] -= 1
    for ele in range(0, len(li)):
        li[ele] = arr[ele]


a = list(map(int, input().split()))
count_sort(a)
for i in a:
    print(i, end=' ')

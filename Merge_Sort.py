# Time Complexity: O(nlogn)
# Auxiliary space: O(n)


def merge_sort(li):
    if len(li) > 1:
        mid = len(li) // 2
        left = li[:mid]  # Dividing list into two halves
        right = li[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while (i < len(left)) and (j < len(right)):  # Copying data to left and right list
            if left[i] < right[j]:
                li[k] = left[i]
                i += 1
            else:
                li[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            li[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            li[k] = right[j]
            j += 1
            k += 1


arr = list(map(int, input().split()))
merge_sort(arr)
for i in arr:
    print(i, end=' ')

# Merge two sorted lists
import random

minValue = 1
maxValue = 999

m = 3
n = 3

nums1_start = [random.randint(minValue, maxValue) for _ in range(m)]
nums1_start.sort()
nums1_end = [0 for _ in range(n)]
nums1 = nums1_start + nums1_end

nums2 = [random.randint(minValue, maxValue) for _ in range(n)]
nums2.sort()

print('Array 1:', nums1)
print('Array 2:', nums2)

def mergeTwoSortedLists(listOne, listTwo):
    if len(listTwo) >= len(listOne): return
    sortedList = listOne
    listTwoPivot = 0

    for i in range(len(listOne)):
        if sortedList[len(sortedList) - 1] > 0: break
        if sortedList[i] > listTwo[listTwoPivot] or sortedList[i] == 0:
            sortedList.insert(i, listTwo[listTwoPivot])
            del sortedList[len(sortedList) - 1]
            listTwoPivot += 1

    return sortedList

sortedList = mergeTwoSortedLists(nums1, nums2)
print('Sorted list result:', sortedList)

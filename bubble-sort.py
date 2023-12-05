import random

def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

def generateArray(arrayLength, minValue, maxValue):
    arr = []

    for _ in range(arrayLength):
        new = random.randint(minValue, maxValue)
        arr.append(new)

    return arr

def bubbleSort(array, start, end):
    if start >= end: return
    lastIndex = partition(array, end)
    bubbleSort(array, start, lastIndex)

def partition(array, end):
    lastIndex = end
    for i in range(end):
        if array[i] > array[i + 1]:
            swap(array, i, i + 1)
    lastIndex = lastIndex - 1
    return lastIndex

startArray = generateArray(10, 0, 50)
print('Start', startArray)

bubbleSort(startArray, 0, len(startArray) - 1)
print('End', startArray)

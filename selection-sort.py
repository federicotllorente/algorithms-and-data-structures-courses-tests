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

def selectionSort(array, start):
    if start >= len(array): return
    orderedUntil = partition(array, start)
    selectionSort(array, orderedUntil)
        
def partition(array, start):
    currentMin = start
    for i in range(start, len(array)):
        if array[i] < array[currentMin]:
            currentMin = i
    swap(array, currentMin, start)
    return start + 1

startArray = generateArray(10, 0, 50)
print('Start', startArray)

selectionSort(startArray, 0)
print('End', startArray)

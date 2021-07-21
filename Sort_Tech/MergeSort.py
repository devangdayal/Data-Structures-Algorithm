# In this Code, We will see Merge Sort Algorithm
# Config Python3

# Merge Sort Implementation Code
def mergeSort(narr,n):
    pass
# TO BE WRITTEN

# Input Array Method
def inputArray(arrLen):
    arr = []
    for x in range(arrLen):
        temp = int(input("Enter the Number ::"))
        arr.append(temp)

    return arr

# Get the Input
n = int(input("Enter the Length of Array ::"))
arr = inputArray(n)

# Sort the Array
arr = mergeSort(arr, n)
print("The Sorted Array ::",arr)

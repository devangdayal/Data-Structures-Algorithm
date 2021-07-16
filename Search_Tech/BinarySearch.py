# In this code, We will be discussing the implementation of Binary Search Algorithm
# Config Python3

# Function to Search the key in the array.

def binarySearch(arr, arrLen, num):
    # Lower Bound of Search
    nLow = 0
    # Higher Bound of Search
    nHigh = arrLen - 1
    center=0

    while (nLow <= nHigh):

        center = (nLow + nHigh) // 2
        # Check whether the number is less than the center

        if (arr[center] > num):
            # In this case , the higher bound is assigned to center
            nHigh = center-1

        #Check whether the number is greater than the center
        elif (arr[center] < num):
            # In this case, the lower bound is assigned to the center
            nLow = center+1
        #Number is in the Center
        else:
            return center

    # In case, the number doesn't exist in the array.
    return -1


# Function to input the array
def inputArray(arrLen):
    arr = []
    for x in range(arrLen):
        temp = int(input("Enter the Number ::"))
        arr.append(temp)

    return arr


# Sorting the array
# Thou we can simply use sort() function given in the python library, but we will use one of the Sorting Algorithm to Sort the array
# In this case,we will use Bubble Sort Technique
def sortArray(arr, arrLen):
    # Need to Traverse thru all the element in the Array
    for x in range(arrLen):
        # Need to Traverse till the last unsorted element

        for y in range(0, arrLen - x - 1):
            # If it is larger than the succeeding number it will perform swap
            if (arr[y] > arr[y + 1]):
                arr[y], arr[y + 1] = arr[y + 1], arr[y]
    return arr


# Get the Input
n = int(input("Enter the Length of Array ::"))
arr = inputArray(n)
# Sort the Array
arr = sortArray(arr, n)
print("The Sorted Array ::",arr)

findNum = int(input("Enter the Number You want to Search ::"))
location = binarySearch(arr, n, findNum)

if (location == -1):
    print("The Number Doesn't Exist..!!")
else:
    print("The Number found at index ::", location+1)

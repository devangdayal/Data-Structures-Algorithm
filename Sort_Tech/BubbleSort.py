# In this code, We will see the BubbleSort Code
# Python3

# Bubble Sort Method
def bubbleSort(narr, nLen):
    # Need to traverse through all the element in the array
    for x in range(nLen):
        # Need to traverse to the last unsorted element
        for y in range(0, nLen - x - 1):
            # Comparing the Adjacent Element
            if narr[y] > narr[y + 1]:
                narr[y], narr[y + 1] = narr[y + 1], narr[y]

    return narr


# Function to input the array
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
arr = bubbleSort(arr, n)
print("The Sorted Array ::", arr)

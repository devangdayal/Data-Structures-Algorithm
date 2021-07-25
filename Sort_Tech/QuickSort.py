# In this code, We will see the Quick Sort Code
# Python3

# Quick Sort Method
def quickSort(narr, nLen):

    pass
# TO BE CONTINUED 


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
arr = quickSort(arr, n)
print("The Sorted Array ::", arr)

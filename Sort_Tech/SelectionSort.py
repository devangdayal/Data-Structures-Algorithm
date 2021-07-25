# In this code, We will see the Selection Sort Code
# Python3

# Selection Sort Method
def selectSort( narr , nLen):

    for x in range(nLen):

        min_value=x

        for y in range (x+1 , nLen):

            if ( narr[min_value] > narr[y]):
                min_value=y

        narr[x],narr[min_value]=narr[min_value],narr[x]

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
arr = selectSort(arr, n)
print("The Sorted Array ::", arr)

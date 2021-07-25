# In this Code, We will see Merge Sort Algorithm
# Config Python3

# Merge Sort Implementation Code
def mergeSort(narr,n):

    if(n>1):

        # Finding the Center of the Array
        center=n//2;

        right_Section=narr[center:]
        left_Section=narr[:center]

        # We will call the array again to cut the array into halves untill it can't be disected anymore
        # i.e. len > 1

        # Sorting the Right Section of the Array
        mergeSort(right_Section,len(right_Section))

        # Sorting the Left Section of the Array
        mergeSort(left_Section, len(left_Section))

        # Reset the Counters
        x=y=z=0

        while ( x < len(left_Section) and y < len(right_Section)):
            # Sorting the Array
            if( left_Section[x] < right_Section[y]):
                narr[z]=left_Section[x]
                x+=1

            else:
                narr[z]=right_Section[y]
                y+=1

            z+=1

        while ( x < len(left_Section)):
            narr[z]=left_Section[x]
            x+=1
            z+=1

        while ( y < len(right_Section)):
            narr[z] = right_Section[y]
            y+=1
            z+=1

    return narr

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

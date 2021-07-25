# Data Structures and Algorithm
 
Data Structures and Algorithm is one of the most important skillset any Aspiring CSE Engineer can possess. 

<em>A data structure is a named location that can be used to store and organize data. And, an algorithm is a collection of steps to solve a particular problem. Learning data structures and algorithms allow us to write efficient and optimized computer programs.</em>

## Visualising the Algorithms
Do Check Out this website to visualise the Sorting Algorithm <br/>
https://visualgo.net/en/sorting

## Sorting Techniques

* Bubble Sorting Technique
  -  Bubble Sort is the sorting algorithm that works by repeatedly swapping the adjacent elements if they are not in proper Order.
  ```
  do

  swapped = false

  for i = 1 to indexOfLastUnsortedElement-1

    if leftElement > rightElement

      swap(leftElement, rightElement)

      swapped = true

  while swapped 
  ```

* Merge Sorting Technique
  - Merge Sort is the sorting algorithm in which firsty it divide the list into the smallest unit (1 element), then compare each element with the adjacent list to sort and merge the two adjacent lists. Finally all the elements are sorted and merged. Merge sort is a divide and conquer algorithm that was invented by John von Neumann in 1945.

  ````
  split each element into partitions of size 1

  recursively merge adjacent partitions

    for i = leftPartIdx to rightPartIdx

      if leftPartHeadValue <= rightPartHeadValue

        copy leftPartHeadValue

      else: copy rightPartHeadValue

  copy elements back to original array

  ````


* Quick Sorting Technique
  - QuickSort is a sorting algorithm based on Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.

````
for each (unsorted) partition

set first element as pivot

  storeIndex = pivotIndex + 1

  for i = pivotIndex + 1 to rightmostIndex

    if element[i] < element[pivot]

      swap(i, storeIndex); storeIndex++

  swap(pivot, storeIndex - 1)

````
* SelectionSort Technique
  - Selection Sort is a sorting algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.
   ````
   repeat (numOfElements - 1) times

     set the first unsorted element as the minimum

     for each of the unsorted elements

       if element < currentMinimum

         set element as new minimum

     swap minimum with first unsorted position

   ````

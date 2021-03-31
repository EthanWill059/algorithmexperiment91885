'''
Python program to compare bubble sort and selection sort, modifed from bubblesort.py

Ethan Williams, March 2021
'''
import random

numamount = int(input("How many numbers do you want? "))

bcomparisons = 0
bswaps = 0
qcomparisons = 0
qswaps = 0

def bubbleSort(arr):
    global bcomparisons
    global bswaps
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element
            bcomparisons += 1
            if arr[j] > arr[j+1] :
                bswaps += 1
                arr[j], arr[j+1] = arr[j+1], arr[j] 

def selectionSort(arr):
    global qcomparisons
    global qswaps

    size = len(arr)
	
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            qcomparisons += 1
            if arr[i] < arr[min_idx]:
                qswaps += 1
                min_idx = i

        # put min at the correct position
        (arr[step], arr[min_idx]) = (arr[min_idx], arr[step])

# Numbers for sorting
arrtouse = [] 
arrtouse2 = []

for i in range (numamount):
    arrtouse = arrtouse + [random.randrange(100)]

arrtouse2 += arrtouse

print ("Unsorted array is:")
print (arrtouse)

selectionSort(arrtouse2)
bubbleSort(arrtouse) # sorting..


print ("\nSorted array is:") 
print(arrtouse)

print("\nBubble Sort:\nComparisons: {} \nSwaps: {}".format(bcomparisons, bswaps))
print("\nSelection Sort:\nComparisons: {} \nSwaps: {}".format(qcomparisons, qswaps))



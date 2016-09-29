#!/usr/bin/python -tt


"""
Input:
Array a[]
n: 1, 2,..,n
1<=n<= 1000
sort: a[], ASC"""

print("***************************************")
print("**************BUBBLE SORT**************")
print("***************************************")
def aBubbleSort(arr):
    for passnum in range(len(arr)-1,0,-1):
        for i in range(passnum):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
print("Please input your number:")
your_number = raw_input('Enter your number: ')
my_array = []
if (your_number <= 5) :
  for i in range(0, your_number - 1):
      x=int(raw_input())
      my_array.append(x)

  print("The entered elements are : ", aBubbleSort(my_array)) 

else:
    print("Restart program")

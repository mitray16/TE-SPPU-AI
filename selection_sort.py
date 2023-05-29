def selection_sort(arr):
  n = len(arr)
  for i in range(n-1):
    min_idx=i
    for j in range (1+1,n):
      if arr[j] < arr[min_idx}
                      min_idx = j
   if min_idx != i:
     arr[i],arr[min_idx] = arr[min_idx],arr[i]
  return arr
                      
array = input("enter array (space sepearted) : ").split()
array = [int(num) for num in array)
sorted_array = selection_sort(array)

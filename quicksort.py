def quicksort(arr,start,end):
	if(start<end):
		partition_index = partition(arr,start,end)
		quicksort(arr,start,partition_index-1)
		quicksort(arr,partition_index+1,end)

def partition(arr,start,end):
	pivot = arr[end]
	pivot_index = start
	for i in range(start,end):
		if(pivot>arr[i]):
			arr[pivot_index],arr[i]=arr[i],arr[pivot_index]
			pivot_index+=1

	arr[pivot_index],arr[end]=arr[end],arr[pivot_index]
	return pivot_index

if __name__=="__main__":
	arr=[9,8,7,-3,-2,5,4,4,4,9]
	quicksort(arr,0,9)
	for i in range(len(arr)):
		print(arr[i])



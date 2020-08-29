arr=[9,3,5,1,0]

for j in range(1,len(arr)):
	i=j-1
	key=arr[j]
	while i>=0 and arr[i]>key:
		arr[i+1]=arr[i]
		i = i-1
	arr[i+1]=key

for i in range(len(arr)):
	print(arr[i])
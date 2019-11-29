def knapsack():
    items = int(input())
    max_weight = int(input())
    values = []
    weights = []
    arr=[[0 for j in range(max_weight+1)]for i in range(items+1)]
    values = list(map(int,input().split()))
    weights = [int(n) for n in input().split()]
    for i in range(items+1):
        for j in range(max_weight+1):
            if i==0 or j==0:
                arr[i][j] == 0
            elif weights[i-1]>j:
                arr[i][j]=arr[i-1][j]
            else:
                arr[i][j]=max(values[i-1]+arr[i-1][j-weights[i-1]],arr[i-1][j])
    print(arr[i][j])
                
if __name__=="__main__":
    test_cases=int(input())
    for i in range(test_cases):
        knapsack()
"""Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of four lines.
The first line consists of N the number of items.
The second line consists of W, the maximum capacity of the knapsack.
In the next line are N space separated positive integers denoting the values of the N items,
and in the fourth line are N space separated positive integers denoting the weights of the corresponding items.
Example:
Input:
2
3
4
1 2 3
4 5 1
2
3
1 2 3
4 5 6
Output:
3
1
"""
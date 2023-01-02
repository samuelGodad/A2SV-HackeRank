def countSwaps(a):
    counter=0
    for i in range(0,n-1):
        for i in range(0,n-1):
            if a[i]>a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                counter+=1
    return counter

n = int(input().strip())
a = list(map(int, input().rstrip().split()))
print("Array is sorted in",countSwaps(a), "swaps.")
print("First Element:",a[0])
print("Last Element:",a[-1])

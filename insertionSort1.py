# Given a sorted list with an unsorted number  in the rightmost cell, can you write some simple code to insert  into the array so that it remains sorted?

# Since this is a learning exercise, it won't be the most efficient way of performing the insertion. It will instead demonstrate the brute-force method in detail.

# Assume you are given the array  indexed . Store the value of . Now test lower index values successively from  to  until you reach a value that is lower than , at  in this case. Each time your test fails, copy the value at the lower index to the current index and print your array. When the next lower indexed value is smaller than , insert the stored value at the current index and print the entire array.

# Example


# Start at the rightmost index. Store the value of . Compare this to each element to the left until a smaller value is reached. Here are the results as described:

# 1 2 4 5 5
# 1 2 4 4 5
# 1 2 3 4 5
def insertionSort1(n, array):
    # Write your code here
    lastElement = arr[-1]
    i = n-1

    while i>0 and arr[i-1] >lastElement:
        arr[i] = arr[i-1]
        print(*arr)
        i-=1

    arr[i] = key
    print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

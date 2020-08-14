'''
Input: a List of integers
Returns: a List of integers
'''
import time

def moving_zeroes(arr):
    # Your code here
    if not arr.count(0):
        return arr
    else:
        # count of non-zero ints
        count = 0
        for i in range(len(arr)):
            # move all non-zeros to the front
            if arr[i] != 0:
                arr[count] = arr[i]
                count +=1
        # replace any values after count to be zero
        for i in range(count,len(arr)):
            arr[i] = 0
        return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    start = time.time()
    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
    print(f"{time.time() - start:.5f}")

    # the runtime of this function is O(n) because we only have to
    # run through the array only twice and we drop any leading numbers.
    # It's linear and the runtime scales with the input data.
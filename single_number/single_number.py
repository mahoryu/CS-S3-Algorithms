'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
import time

def single_number(arr):
    # Your code here
    for item in arr:
        if arr.count(item) == 1:
            return item

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    start = time.time()
    print(f"The odd-number-out is {single_number(arr)}")
    print(f"{time.time() - start:.5f}")

    # runtime is O(n) because the function runs through the
    # array only once.
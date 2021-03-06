'''
Input: a List of integers
Returns: a List of integers
'''
import time

def product_of_all_other_numbers(arr):
    # Your code here
    copy = arr.copy()
    for i in range(len(copy)):
        product = 1
        for j in range(len(copy)):
            if i == j:
                continue
            else:
                product *= copy[j]
        arr[i] = product
    return arr

#TODO Memoization

# def product_of_all_other_numbers_v2(arr):
#     full_prod = 1
#     for num in arr:
#         full_prod *= num

#     for i in range(len(arr)):
#         arr[i] = full_prod / arr[i]
#     return arr

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    start = time.time()
    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
    print(f"{time.time() - start:.5f}")

    # start = time.time()
    # print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers_v2(arr)}")
    # print(f"{time.time() - start:.5f}")
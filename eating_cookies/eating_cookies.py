'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, curr = 0):
    if n is None:
        return
    elif n == 0:
        return n + 1
    else:
        while curr is not n:
            curr = curr + 1
        return curr
    # if n is 0:
    #     return n 
    # return eating_cookies(n, curr + 1)

    # if curr is n:
    #     return n
    # else:
    #     while curr is n:
    #         n = n - 1
    #     return eating_cookies(n, curr + 1)
    # if curr is n:
    #     return n
    # else:
    #     if curr <= n:
    #         curr = curr + 1
    #         return eating_cookies(n - 1)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")

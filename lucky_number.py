
# inputs = [103,225,997]


def discard_nth(n_list, x, n):
    del n_list[x::n]

def is_lucky():
    inp = int(input("Enter a positive integer: "))
    nums = list(range(1, inp*3))
    i = 1
    x = nums[0]
    discard_nth(nums, x, x+1)
    while x <= inp:
        x = nums[i]
        discard_nth(nums, x-1, x)
        i += 1
    if inp in nums:
        print(str(inp) + " is a lucky number")
    else: 
        ind = min(range(len(nums)), key = lambda i: abs(nums[i] - inp))
        if nums[ind] > inp:
            print(str(nums[ind - 1]) + ' < ' + str(inp) + ' < ' + str(nums[ind]))
        else:
            print(str(nums[ind]) + ' < ' + str(inp) + ' < ' + str(nums[ind+1]))

if __name__ == "__main__":
    import sys
    is_lucky()
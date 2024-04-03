nums = [1, 2, 3, 4, 3, 22, 1]


def checkDuplicate(nums):
    for i in range(len(nums)):
        cur = nums[i]
        for j in range(i + 1, len(nums)):
            if cur == nums[j]:
                return True
    return False


print(checkDuplicate(nums=nums))

# O(n^2)


# better way, sort it, so we only iterate once
# sorting time O(nlogn) and space O(1)


# hashset is even better


def checkDuplicate2(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

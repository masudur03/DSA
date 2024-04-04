
# brute force solution O(n^2)
def twoSum(nums, target):
    for i in range(len(nums) - 1):
        cur = nums[i]
        for j in range(i + 1, len(nums)):
            if (cur + nums[j]) == target:
                return [i, j]


# better solution make a hashmap
def twoSum2(nums, target):
    # create a hashpmap
    num_map = {}
    # loop through the nums array
    for i in range(len(nums)):
        cur = nums[i]
        diff = target - cur

        # cheking if sum key  exist
        if diff in num_map:
            # return the curent num index and sum's index
            return [i, num_map[diff]]
        else:
            # add the cur num into the map
            num_map[cur] = i  # map the num with its index

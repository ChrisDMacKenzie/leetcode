def removeDuplicates(nums: list[int]) -> int:
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j += 1
    return j

if __name__ == "__main__":
    s1 = removeDuplicates([1,1,2])
    print(s1)
    s2 = removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    print(s2)
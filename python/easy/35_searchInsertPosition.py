def searchInsert(nums: list[int], target: int) -> int:
    for i, v in enumerate(nums):
        if v == target:
            return i
        elif v > target:
            return i
    return len(nums)

if __name__ == "__main__":
    s1 = searchInsert([1,3,5,6], 5)
    print(s1)
    s2 = searchInsert([1,3,5,6], 2)
    print(s2)
    s3 = searchInsert([1,3,5,6], 7)
    print(s3)
def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, v in enumerate(nums):
        remaining = target - v
        if remaining in seen:
            return [i, seen[remaining]]
        seen[v] = i

if __name__ == "__main__":
    s1 = twoSum([2,7,11,15], 9)
    print(s1)
    s2 = twoSum([3,2,4], 6)
    print(s2)
    s3 = twoSum([3,3], 6)
    print(s3)
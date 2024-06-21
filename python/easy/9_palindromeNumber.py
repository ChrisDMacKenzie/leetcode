def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

if __name__ == "__main__":
    s1 = isPalindrome(121)
    print(s1)
    s2 = isPalindrome(-121)
    print(s2)
    s3 = isPalindrome(10)
    print(s3)
def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if len(stack) > 0 and stack[-1] == mapping[char]:
                stack.pop(-1)
            else:
                return False
    return len(stack) == 0

if __name__ == "__main__":
    s1 = isValid("()")
    print(s1)
    s2 = isValid("()[]{}")
    print(s2)
    s3 = isValid("(]")
    print(s3)
def longestCommonPrefix(strs: list[str]) -> str:
    prefix = ""
    wordLengths = [len(word) for word in strs]
    minLength = min(wordLengths)
    i = 0
    while i < minLength:
        isCommon = True
        char = strs[0][i]
        for word in strs:
            if word[i] != char:
                isCommon = False
        if isCommon == False:
            break
        prefix += char
        i += 1
    return prefix


if __name__ == "__main__":
    s1 = longestCommonPrefix(["flower","flow","flight"])
    print(s1)
    s2 = longestCommonPrefix(["dog","racecar","car"])
    print(s2)
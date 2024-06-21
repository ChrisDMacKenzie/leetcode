def lengthOfLastWord(s: str) -> int:
    wordArray = s.split()
    return len(wordArray[-1])

if __name__ == "__main__":
    s1 = lengthOfLastWord("Hello World")
    print(s1)
    s2 = lengthOfLastWord("   fly me   to   the moon  ")
    print(s2)
    s3 = lengthOfLastWord("luffy is still joyboy")
    print(s3)
def romanToInt(s: str) -> int:
    intValue = 0
    for i, v in enumerate(s):
        if v == 'I':
            if len(s) > i+1 and s[i+1] in ['V', 'X']:
                intValue += -1
            else:
                intValue += 1
        elif v == 'V':
            intValue += 5
        elif v == 'X':
            if len(s) > i+1 and s[i+1] in ['L', 'C']:
                intValue += -10
            else:
                intValue += 10
        elif v == 'L':
            intValue += 50
        elif v == 'C':
            if len(s) > i+1 and s[i+1] in ['D', 'M']:
                intValue += -100
            else:
                intValue += 100
        elif v == 'D':
            intValue += 500
        elif v == 'M':
            intValue += 1000
    return intValue

if __name__ == "__main__":
    s1 = romanToInt("III")
    print(s1)
    s2 = romanToInt("LVIII")
    print(s2)
    s3 = romanToInt("MCMXCIV")
    print(s3)
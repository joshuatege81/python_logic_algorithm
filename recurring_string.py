#Given the string as an example AAABCC, and the output will be A. It output the character that appear the most

def recurring(string):
    counts = {}
    for i in string:
        if i in counts:
            return i
        counts[i] = 1
    return None

string = str(input())
string = [str(x) for x in string]

print(recurring(string))
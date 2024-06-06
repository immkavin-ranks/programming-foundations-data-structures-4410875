# O(n)
def is_matching_paren(s):
    parenthesis = []
    for c in s:
        if c == "(":
            parenthesis.append(c)
        elif c == ")":
            if not parenthesis:
                return False
            parenthesis.pop()
    return len(parenthesis) == 0

print(is_matching_paren("(k(a))"))
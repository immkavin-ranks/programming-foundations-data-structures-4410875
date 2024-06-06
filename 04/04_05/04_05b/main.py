def has_unique_characters(data):
    string_set = set(data) # O(n) linear
    return len(data) == len(string_set)

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))

def all_variants(text):
    i = 0
    while i != len(text):
        yield text[i]
        i += 1
    i = 0
    while i != len(text) - 1:
        yield text[i] + text[i+1]
        i += 1
    i = 0
    while i != len(text) - 2:
        yield text[i] + text[i+1] + text[i+2]
        i += 1

a = all_variants("abc")
for i in a:
    print(i)
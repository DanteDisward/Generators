def all_variants(text):
    for q in range(len(text)):
        for j in range(len(text) - q):
            yield text[j:j + q + 1]


a = all_variants("abc")
for i in a:
    print(i)

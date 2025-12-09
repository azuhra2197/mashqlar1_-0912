# 1
kvadratlar = [n**2 for n in range(1, 11)]
print(kvadratlar)

# 2
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 3
toq_sonlar = [i for i in range(10, 31) if i % 2 == 1]
print(toq_sonlar)

# 4
words = ["apple", "banana", "pear"]
lengths = [len(w) for w in words]
print(lengths)

# 5
soz = "So'z"
harflar = list(soz)
print(harflar)

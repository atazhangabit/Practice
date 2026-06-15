text = input().split()

words = []
counts = []

for word in text:
    if word in words:
        index = words.index(word)
        counts[index] = counts[index] + 1
    else:
        words.append(word)
        counts.append(1)

for i in range(len(words)):
    print(words[i] + ": " + str(counts[i]))
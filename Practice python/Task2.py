s = input()

longest = ""
current = ""

for ch in s:
    if current == "":
        current = ch
    else:
        if ch > current[-1]:
            current = current + ch
        else:
            if len(current) > len(longest):
                longest = current
            current = ch

if len(current) > len(longest):
    longest = current

print(longest)
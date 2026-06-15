s = input()

result = ""

for ch in s:
    if ch >= "0" and ch <= "9":
        result = result + ch

if result == "":
    print(0)
else:
    print(result)
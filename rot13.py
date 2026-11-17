text = "Hello world"

result = ""

for c in text:
    if "a" <= c <= "z":
        result += chr((ord(c) - ord("a") + 13) % 26 + ord("a"))
    else:
        result += c

print(result)

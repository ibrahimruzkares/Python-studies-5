words = ["automobile", "car", "anger", "fox", "anchor"]

words = [word.upper() if word.startswith("a") else word for word in words]
print(words)


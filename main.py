reviews = ["Very good product. perfect delivery good .... :)",
           "bad bad bad",
           "good good"]

allwords = {}

sen = "a,b,c"

for sentence in reviews:
    for word in sentence.split(" "):
        if word not in allwords:
            allwords[word] = 1
        else:
            allwords[word] += 1

print(allwords)
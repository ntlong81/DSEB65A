text = "google.com"
count = {}
for t in text:
    if t not in count:
        count[t] = 1
    else:
        count[t] += 1
print(count)
          
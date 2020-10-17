
with open('homework2.txt','r') as f:
    lines = f.readlines()

related_coffee=[]
for line in lines:
    groceries = line.split(',')
    if 'coffee' in groceries:
        related_coffee.append(groceries)

related_coffee2 = []
for a in related_coffee:
    a = set(a)
    a.remove('')
    a.remove('\n')
    a = list(a)
    related_coffee2.append(a)

related_coffee3 = []
for a in related_coffee2:
    related_coffee3 = related_coffee3 + a
for a in related_coffee3:
    if a.split('.')[0] == '2019':
        related_coffee3.remove(a)


word_counts = {word:related_coffee3.count(word) for word in set(related_coffee3)}
word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
for i in range(1,6):
    print(word_counts[i])



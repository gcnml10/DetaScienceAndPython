with open('homework2.txt', 'r') as f:
    lines = f.readlines()

def find_related_groceries(grocery):
    related_grocery = []
    for line in lines:
        groceries = line.strip().split(',')
        if grocery in groceries:
            related_grocery.append(groceries)
    if len(related_grocery) == 0:
        print('None')
        return None
    related_grocery2 = []
    for a in related_grocery:
        a = set(a)
        a = list(a)
        related_grocery2.append(a)
    #그냥 달 만들기
    month = []
    for i in range(1, 10):
        a = '2019.0' + str(i)
        month.append(a)
    for i in range(10,13):
        a = '2019.' + str(i)
        month.append(a)
    count = 0
    result = {}
    for month in month:
        count += 1
        month_list = []
        for one in related_grocery2:
            if month in one:
                month_list = month_list + one
        word_counts = {word: month_list.count(word) for word in set(month_list) if not word.startswith('2019') and len(word) >0}
        del word_counts[grocery]
        word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        temp = []
        for i in range(0,3):
            temp.append(word_counts[i])
        temp = dict(temp)
        result[month] = temp
    print(result)
    return result

find_related_groceries('butter')




# related_grocery3 = []
# for a in related_grocery2:
#     related_coffee3 = related_grocery3 + a
# for a in related_grocery3:
#     if a.split('.')[0] == '2019':
#         related_grocery3.remove(a)
#
#
# word_counts = {word:related_coffee3.count(word) for word in set(related_coffee3)}
# word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
# for i in range(1,6):
#     print(word_counts[i])

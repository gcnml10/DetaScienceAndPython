import re
from collections import Counter

with open('./pubmed-coronaviru-set.txt/pubmed-coronaviru-set.txt', 'r', encoding='utf8') as f:
    lt = []
    for line in f.readlines():
        if line.startswith('DP'):
           lt.append(line)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_list = [[month,0] for month in months]
for month in month_list:
    for date in lt:
        if month[0] in date:
            month[1] += 1

month_list = sorted(month_list, key=lambda x:x[1], reverse=True)
print(month_list)


with open('./pubmed-coronaviru-set.txt/pubmed-coronaviru-set.txt', 'r', encoding='utf8') as f:
    lt = []
    lastLt = []
    count = 0
    for line in f.readlines():
        if line.startswith('   '):
            lt[-1] = lt[-1] + line
        else:
            lt.append(line)
    dict = {}
    for line in lt:
        if line.startswith("PMID"):
            count += 1
            dict[count] = [line]
        else:
            dict[count] = dict[count] + [line]
    print(len(dict.values()))
    adDict = {}
    count2 = 0
    for ads in dict.values():
        count2 += 1
        for i in ads:
            if i.startswith('AD'):
                adDict[count2] = i
        # try:
        #     adDict[count2]
        # except:
        #     adDict[count2] = 'None'

    print(len(adDict))
    finalLines = list(adDict.values())
    for line in finalLines:
            result = re.findall('\s[A-Z]+[a-zA-Z]+[.]$',line)                              #'\s+?[a-z]+[.]$'
            if len(result) >0:
                lastLt.extend(result)
    lastLt = [result.replace(' ','').replace('.','') for result in lastLt]

print(len(lastLt))
lt2 = Counter(lastLt).most_common()
print(lt2)


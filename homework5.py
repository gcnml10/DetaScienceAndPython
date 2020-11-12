# with open('./pubmed-coronaviru-set.txt/pubmed-coronaviru-set.txt', 'r', encoding='utf8') as f:
#     lt = []
#     for line in f.readlines():
#         if line.startswith('DP'):
#            lt.append(line)
# print(lt)
#
# May = 0
# for date in lt:
#     if 'May' in date:
#         May+=1
# print(May)

# import re
# from collections import Counter
#
# with open('./pubmed-coronaviru-set.txt/pubmed-coronaviru-set.txt', 'r', encoding='utf8') as f:
#     lt = []
#     for line in f.readlines():
#         result = re.findall('\s[A-D]+[a-z]*[.]$',line)                              #'\s+?[a-z]+[.]$'
#         if len(result) >0:
#             # result.strip()
#             lt.extend(result)
# lt2 = Counter(lt).most_common()
# print(lt2)

import re
from collections import Counter
#
# with open('./pubmed-coronaviru-set.txt/pubmed-coronaviru-set.txt', 'r', encoding='utf8') as f:
#     line = ''
#
#
#     # # for line in f.readlines():
#     while True:
#         print(f.readline())
#
#     # lt3 = []
    # lines = ''
    # for line in f.readlines():
    #     if line.startswith('AD'):
    #         print(line)
    #         a='aa'
    #         while line.endswith('.') == False:
    #             line = f.readline()
    #             print(line)
    #         result = re.findall('\s[A-za-z]*[.]$',line)
    #         lt3.append(result)
    #         print(result)


# # print(lt3)AD  - School of Medicine, The Maldives National University, Male', Maldives.
# a = "AD  - School of Medicine, The Maldives National University, Male', Maldives."
# # print(a)
# # print(re.findall('\s[A-za-z]*[.]$', a))
# # print(len(re.findall('\s[A-za-z]*[.]$', a)))
# print(a.endswith('.'))


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
        try:
            adDict[count2]
        except:
            adDict[count2] = 'None'

    finalLines = list(adDict.values())
    print(len(adDict))
    print(len(finalLines))
    print(finalLines)
    for line in finalLines:
            result = re.findall('\s[A-Z]+[a-zA-Z]+[.]$',line)                              #'\s+?[a-z]+[.]$'
            if len(result) >0:
            # result.strip()
                lastLt.extend(result)
# print(lastLt)
print(len(lastLt))
lt2 = Counter(lastLt).most_common()
print(lt2)


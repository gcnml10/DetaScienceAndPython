dict = {1: '1', 3: '3'}
try:
    dict[2]
except:
    dict[2] = 'None'
print(dict)
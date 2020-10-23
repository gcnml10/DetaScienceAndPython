from homework4_prac import related_groceries as desa

# 조건 1
print("조건 1번")
desa().all_frequency()

# 조건 2
print("조건 2번")
a = desa().sales_together('whole milk', 'fruit')
print(a)

# 조건 3
print("조건 3번")
b = desa().frequency_fit_to_condition('coffee')
print(b)

# 조건 4
print("조건 4번")
c = desa().Jaccard_between_two('whole milk', 'pip fruit')
print(c)

# 조건 5
print("조건 5번")
d = desa().Whole_Jaccard(0.8)
print(d)

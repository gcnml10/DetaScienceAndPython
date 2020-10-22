from homework4_prac import related_groceries as desa

# result_dict = desa('whole milk').find_related_groceries()
# print(result_dict)
# for k,v in result_dict.items():
#     print(k, v)
#
# result = desa("whole milk", 'coffee').both_in_lines(3)
# print(result)

result = desa('coffee').frequency()
print(result)
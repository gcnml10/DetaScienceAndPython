from collections import Counter

#라인 다 뽑기
all_lines = []
with open('homework2.txt','r',encoding='utf8') as input_file:
    for line in input_file.readlines():
        all_lines.append(line)

#0~12 아니면 None / 0이면 모든 라인 / 해당 달의 라인만 추출
def get_month_lines(month=0):
    if month not in range(0,13): return None
    if not month:
        return all_lines
    month_str = '2019.' + str(month).zfill(2)
    return [line for line in all_lines if line.startswith(month_str)]

#keyword가 들어있는 라인 모두 추출
def get_all_lines_with_keyword(keyword):
    return [line for line in all_lines if keyword in line]

#달 뽑는 함수에서 None 나오면 None / 특정 달 추출한 리스트에서 keyword가 들어있는 라인만 추출
def get_lines_with_keyword(keyword, month=0):
    month_lines = get_month_lines(month)
    if month_lines is None:
        return None
    return [mline for mline in month_lines if keyword in mline]


def find_related_groceries(grocery, common_number=3):
    total_dict = {}
    for month in range(1, 13):
        month_groceries = []
        month_lines = get_lines_with_keyword(grocery, month)  #month와 keyword=grocery 넣고 특정 달에서 keyword가 있는 라인 추출
        for mline in month_lines:
            groceries = [item for item in mline.strip().split(',')
                         if len(item) > 1 and not item.startswith('2019')
                         and item != grocery]                 #위에서 추출한 keyword와 month 일치하는 라인에서 keyword 제외한 모든 item 추출
            month_groceries.extend(groceries)

        #calc freg
        month_counter = Counter(month_groceries)              #item 개수 counter 함수로 딕셔너리 정리
        month_str = '2019.' + str(month).zfill(2)
        top3_groceries = month_counter.most_common(common_number) #{'coffee':3, 'yougurt': 2 ~~~} 이렇게 위에서 정리한 month_counter에서 common_number=3 개만 추출
        total_dict[month_str] = {gtuple[0]: gtuple[1] for gtuple in top3_groceries}  #{'coffee':3} 이런 gtuple을 하나씩 뽑아서 [0]= 식료품이름 [1]= 개수 해서 딕셔너리로 넣고 그 {} 통째로 month_str(월별로) 정리
    return total_dict

result_dict = find_related_groceries('coffee')
print(result_dict)
for k,v in result_dict.items():
    print(k, v)

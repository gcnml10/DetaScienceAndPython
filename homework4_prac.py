from collections import Counter


class related_groceries:

    def __init__(self):

        # 라인 다 뽑기
        all_lines = []
        with open('homework2.txt', 'r', encoding='utf8') as input_file:
            for line in input_file.readlines():
                all_lines.append(line)
        self.all_lines = all_lines

    # 0~12 아니면 None / 0이면 모든 라인 / 해당 달의 라인만 추출
    def get_month_lines(self, month=0):
        if month not in range(0, 13): return None
        if not month:
            return self.all_lines
        month_str = '2019.' + str(month).zfill(2)
        return [line for line in self.all_lines if line.startswith(month_str)]

    # keyword가 들어있는 라인 모두 추출
    def get_all_lines_with_keyword(self, grocery):
        return [line for line in self.all_lines if grocery in line]

    # 달 뽑는 함수에서 None 나오면 None / 특정 달 추출한 리스트에서 keyword가 들어있는 라인만 추출
    def get_lines_with_keyword(self, grocery, month=0):
        month_lines = self.get_month_lines(month)
        if month_lines is None:
            return None
        return [mline for mline in month_lines if grocery in mline]

    # grocery와 같이 판매된 top3 상품 월별 조회
    def find_related_groceries(self, grocery, common_number=3):
        total_dict = {}
        for month in range(1, 13):
            month_groceries = []
            month_lines = self.get_lines_with_keyword(grocery,
                                                      month)  # month와 keyword=grocery 넣고 특정 달에서 keyword가 있는 라인 추출
            for mline in month_lines:
                groceries = [item for item in mline.strip().split(',')
                             if len(item) > 1 and not item.startswith('2019')
                             and item != grocery]  # 위에서 추출한 keyword와 month 일치하는 라인에서 keyword 제외한 모든 item 추출
                month_groceries.extend(groceries)

            # calc freg
            month_counter = Counter(month_groceries)  # item 개수 counter 함수로 딕셔너리 정리
            month_str = '2019.' + str(month).zfill(2)
            top3_groceries = month_counter.most_common(
                common_number)  # {'coffee':3, 'yougurt': 2 ~~~} 이렇게 위에서 정리한 month_counter에서 common_number=3 개만 추출
            total_dict[month_str] = {gtuple[0]: gtuple[1] for gtuple in
                                     top3_groceries}  # {'coffee':3} 이런 gtuple을 하나씩 뽑아서 [0]= 식료품이름 [1]= 개수 해서 딕셔너리로 넣고 그 {} 통째로 month_str(월별로) 정리
        return total_dict

    ################################################################### 중간고사 이전
    ################################################################### 중간고사 이후

    # 2개의 식품 월별 같이 판매된 라인
    def both_in_lines(self, grocery, grocery2, month=0):
        both = []
        month_lines = self.get_month_lines(month)
        try:
            for line in month_lines:
                if grocery in line and grocery2 in line:
                    both.append(line)
            return both
        except Exception as e:  # 에러 발생시 에러 프린트
            print(e)
            return None

    # 월별 빈도 반환
    def frequency(self, grocery):
        pre_list = {}
        pre_list['grocery_name'] = grocery
        for month in range(1, 13):
            count = 0
            month_lines = self.get_lines_with_keyword(grocery,
                                                      month)  # month와 keyword=grocery 넣고 특정 달에서 keyword가 있는 라인 추출
            for mline in month_lines:
                count += 1  # 판매된 라인 보일 때마다 count 1씩 증가
            pre_list[month] = count
        frequency = pre_list
        return frequency

    # 중복없는 식료품 목록 생성
    def set_of_groceries(self):
        all_groceries = []
        for line in self.all_lines:
            temp = [item for item in line.strip().split(',')
                    if len(item) > 1 and not item.startswith('2019')]
            all_groceries.extend(temp)
        set_groceries = set(all_groceries)
        return set_groceries

    # 모든 식료품의 월별 빈도 csv파일로 저장
    def all_frequency(self):
        set_groceries = self.set_of_groceries()
        f = open('mid-term_01_동주.csv', 'w')
        f.write("grocery_name,01,02,03,04,05,06,07,08,09,10,11,12\n")
        for item in set_groceries:
            frequency = self.frequency(item)
            f.write(str(tuple(frequency.values())).strip('(').strip(')').strip("'").strip(
                "'"))  # tuple('grocery',,,) 형태이 데이터를 저장하기 위해 1,2,3 과 같은 형태로 변환
            f.write('\n')  # 개행문자 삽입
        f.close()
        return print("Success")

    # 2개의 식료품이 같이 판매된 빈도/월별순서의 크기 12인 리스트 반환
    def sales_together(self, grocery1, grocery2):
        month_list = [line for line in self.all_lines if grocery1 in line and grocery2 in line]  # 같이 판매된 라인을 먼저 찾고
        count_dic = {}
        for month in range(1, 13):
            month_str = '2019.' + str(month).zfill(2)
            count_dic[month_str] = 0
            for together in month_list:
                if together.startswith(month_str):  # 라인에 있는 month로 월별로 정리 및 count
                    count_dic[month_str] += 1
                    month_list.remove(together)
        together_list = list(count_dic.values())

        return together_list

        # 조건 3에 맞도록 크기가 12이며, 1월부터 12월 순으로 반환

    def frequency_fit_to_condition(self, grocery):
        fre_list = list(self.frequency(grocery).values())
        del fre_list[0]

        return fre_list

        # 두 식품간의 유사도 계산

    def Jaccard_between_two(self, grocery1, grocery2):
        Sk = self.frequency_fit_to_condition(grocery1)  # 각각 월별 판매빈도를 가져온다
        Tk = self.frequency_fit_to_condition(grocery2)
        Jaccard = self.Jaccard_formula(Sk, Tk)
        return Jaccard

    def Jaccard_formula(self, Sk, Tk):
        numerator = []
        denominator = []
        for i in range(0, 12):
            denominator.append(max(Sk[i], Tk[i]))  # 두 수에서 작은 값은 분자에, 큰 값은 분모에 넣는다
            numerator.append(min(Sk[i], Tk[i]))
        Jaccard = sum(numerator) / sum(denominator)
        return Jaccard

        # 전체 식품에서 threshold 초과의 jaccard print

    def Whole_Jaccard(self, threshold):
        set_of_groceries_01 = self.set_of_groceries()  # 두개의 grocery_set 준비
        set_of_groceries_02 = self.set_of_groceries()

        frequency_set = {}
        set_groceries = self.set_of_groceries()
        for item in set_groceries:
            frequency = self.frequency_fit_to_condition(item)
            frequency_set[item] = frequency

        frequency_set_01 = frequency_set
        frequency_set_02 = frequency_set

        for item_01 in set_of_groceries_01:
            for item_02 in set_of_groceries_02:
                if item_01 == item_02:
                    continue  # 자기 자신이면 continue로 넘어가기
                else:
                    Jaccard = self.Jaccard_formula(frequency_set_01[item_01], frequency_set_02[item_02])
                    if Jaccard > threshold:  # threshold 초과시 print
                        print(str(item_01) + ", " + str(item_02) + ", " + str(Jaccard))
            set_of_groceries_02.remove(item_01)  # 중복계산을 피하기 위해 두번째 반복문의 set에서 삭제

        print('success')

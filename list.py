subway = ["빨강", "주황", "노랑"]
print(subway)

#주황은 몇 번째 칸에 타고 있는가?
print(subway.index("주황"))

#초록이가 다음 정류장에서 다음 칸에 탐
subway.append("초록")
print(subway)

#검정이를 주황과 노랑 사이에 태움
subway.insert(2, "검정")
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
subway.pop()   #초록이 내림
print(subway)
subway.pop()   #노랑이 내림
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("빨강")
print(subway.count("빨강"))

#오름차순 정렬
num_list = [1, 5, 4, 3, 2]
num_list.sort()
print(num_list)

#내림차순 정렬
num_list.sort(reverse = True)
print(num_list)

#순서 뒤집기
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#리스트 확장
num_list = [1, 2, 3]
num_list2 = [4, 5, 6]
num_list.extend(num_list2)
print(num_list)
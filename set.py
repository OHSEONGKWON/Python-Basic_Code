#집함
#중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"빨강", "주황", "노랑"}
python = set(["빨강", "초록"])

#교집함 (java와 python 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합 (java도 할 수 있거나 python도 할 수 있는 개발자)
print(java | python)
print(java.union(python))

#차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

#python 할 줄 아는 사람이 늘어남
python.add("파랑")
print(python)

#java를 잊었어요
java.remove("빨강")
print(java)
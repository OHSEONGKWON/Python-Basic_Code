cabinet_num = {3:"빨강", 100:"주황"}
print(cabinet_num[3])
print(cabinet_num[100])

print(cabinet_num.get(3))
print(cabinet_num.get(100))
print(cabinet_num.get(5, "사용가능"))

print(3 in cabinet_num)  #True
print(5 in cabinet_num)  #True

cabinet_str = {"A-1":"노랑", "B-1":"초록"}
print(cabinet_str["A-1"])
print(cabinet_str["B-1"])

#새 손님
cabinet_str["A-1"] = "파랑"
cabinet_str["C-1"] = "남색"
print(cabinet_str)

#간 손님
del cabinet_str["B-1"]   #초록이 감
print(cabinet_str)

#key 들만 출력
print(cabinet_str.keys())
print(cabinet_str.values())

#key, value 쌍으로 출력
print(cabinet_str.items())

#폐점
cabinet_str.clear()
print(cabinet_str)

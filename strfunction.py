python = "Python is Amazing"
print(python.lower())  # 소문자 출력
print(python.upper())  # 대문자 출력
print(python[0].isupper())  # 대문자인가?
print(len(python))  # 문자열 길이
print(python.replace("Python", "Java"))  # 단어 변경

print(python.index("n"))  # n은 몇 번째에 있는가?
index = python.index("n")
print(python.index("n",index + 1))  # 다음 n은 몇 번째에 있는가?

print(python.find("Java"))  # Java라는 문자를 찾아
print(python.count("n"))  # n은 총 몇 개 있는가?
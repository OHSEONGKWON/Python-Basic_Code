# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com 
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

# 예) 생성된 비밀번호 : nav51!

url = "http://naver.com"
url = url.replace("http://", "")
url = url[:url.index(".")]
password = url[:3]

password2 = url[:url.index("v")] + str(len(password)) + str(password.count("n")) + "!"
print(password2)
print("{password}{number}{number2}!".format(password = url[:3], number = len(url), number2 = url.count("e")))
print("나는 %d살 입니다." %20)
print("나는 %s를 좋아해요." %"농구")
print("Apple은 %c로 시작해요." %"A")
print("나는 %s살 입니다." %23)
print("나는 %s색과 %s색을 좋아해요." %("하얀", "검정"))

print("나는 {}살 입니다.".format(23))
print("나는 {}색과 {}색을 좋아해요".format("하얀", "검정"))
print("나는 {0}색과 {1}색을 좋아해요.".format("하얀", "검정"))
print("나는 {1}색과 {0}색을 좋아해요.".format("하얀", "검정"))

print("나는 {age}살 이며, {color}색을 좋아해요".format(age = 23, color = "하얀"))

age = 23
color = "하얀"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
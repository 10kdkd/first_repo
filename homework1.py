# # 1-1
# x = 0
# y = 0
# while x < 1000:
#     if x % 3 == 0:
#         y += x
#     x += 1
# print(y)

# 1-2
# x = 10
# while x > 0:
#     print('*'*x)
#     x += -1

# 1-3
# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# A.sort()
# A.reverse()
# x = 0
# i = 0
# while A[i] >= 50 :
#     x += A[i]
#     i += 1
# print(x)

# 2-1
# for i in range(1,101):
#     print(i)

# 2-2
# A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# x = 0
# for i in A:
#     x += i
# print(x/len(A))

# 2-3
# number = [1, 2, 3, 4, 5]
# result = [n*2 for n in number if n%2 == 1]
# print(result)

# 연습문제(리스트 내장함수)
# A = ['Life', 'is', 'too', 'short']
# s = ' '
# print(s.join(A))

# 연습문제(if)
# a = 'Life is too short, you need python'
# if 'wife' in a:
#     print('wife')
# elif 'python' in a and 'you' not in a:
#     print('python')
# elif 'shirt' not in a:
#     print('shirt')
# elif 'need' in a:
#     print('need')
# else:
#     print('none')
# 결과로 'shirt' 나오게 된다.

# 연습문제(while)
# x=1
# while x < 5:
#     print(x * '*')
#     x += 1

# 연습문제(모음 찾기)
# A = 'mutzangesazachurum'
# x = 0
# for i in A:
#     if i in 'aeiou':
#         x += 1
#     else:
#         continue
# print(x)
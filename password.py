password = 'a123456'
print('您最多有3次输入密码的机会')
i = 3
while i > 0:
	password1 = input('请输入密码： ')
	if password1 == password:
		print('登入成功')
		break
	else:
		i = i - 1
		print('密码错误！还有', i, '次机会')
if i == 0:
	print('您密码错误次数过多，无法再次输入')
# author:Sole_idol
# filename: test.py
# datetime:2020/8/18 11:31

# li = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
li = []
for i in li:
    print(i)
    if i == 'ccc':
        break
else:   # 程序自然死亡会运行,当列表为空，肯定也是自然死亡，所以会运行
    print('这是一个空列表')

# for循环语句中的自然死亡，就是没有遇到break，而是，对象遍历完后跳出的
# 当通过break跳出循环语句，就不是自然死亡，就不会运行else后面的语句

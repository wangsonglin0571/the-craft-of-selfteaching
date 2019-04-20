#<first edit> 自学是门手艺
#不是学会学习，而是学会自学
#narrow down your topic
#把时间当作朋友
#通往财富自由之路
#韭菜的自我修养
#背后目标都是 学习 进步 甚至是进化
#自学能力，是持续学习持续成长的发动机
 #至少有99%的人终生都没有掌握自学能力
 #有人带，有人教，有人逼的情况下都没有真学明白那些基础知识
 #应试教育是磨灭自学能力最有效的方法
 #一切与自学相关的技巧都是老生常谈
 

def say_hi(*names):
    for name in names:
        print(f'Hi,{name}!')


print(say_hi())
print(say_hi('ann'))
print(say_hi('mike','john','zeo'))

a_string = 'Python'
print(say_hi(*a_string))

names = ('mike', 'john', 'zeo')
print(say_hi(*names))


#化名，匿名 alias
# 能被4整除的是闰年
# 能被100整除，但不能被400整除的不是闰年
def _is_leap(year):
    return year % 4 ==0 and (year % 100 !=0 or year % 400 == 0)

year_leap_bool = _is_leap
print(year_leap_bool(800))

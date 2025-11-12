#1.输出hello world
"""from pandas.core.computation.ops import isnumeric

print("Hello World！\n___May")
#2.计算两个数字之和
num1=float(input("输入第一个数字："))
num2=float(input("输入第二个数字："))
print("{0}和{1}相加的结果为{2}:".format(num1,num2,num1+num2))
print("两数之和为%.1f"%(float(input("输入第一个数字："))+float(input("输入第二个数字："))))
#计算平方根
num=float(input("需要开平方的数字是："))
num_sqrt=num**0.5
print("%.3f的平方根为%.3f"%(num,num_sqrt))
import cmath # 计算实数和复数平方根，导入复数数学模块
num=float(input("需要开平方的数字是："))
num_sqrt=cmath.sqrt(num)
print("{0:.3f}的平方根为{1:.3f}+{2:.3f}j".format(num,num_sqrt.real,num_sqrt.imag))
# 3.程序功能: 求解二次方程 ax**2 + bx + c = 0
# 注意: a ≠ 0，a、b、c 为用户输入的实数
import cmath
def get_float_input(prompt):

        #获取用户输入的浮点数，并处理非法输入。:param prompt: 提示信息。:return: 用户输入的浮点数
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("请输入有效的数字！")
def solve_quadratic(a,b,c):

        #计算二次方程的解。:param a: 二次项系数。:param b: 一次项系数。:param c: 常数项。:return: 二次方程的两个解
    descriminant=b**2-4*a*c
    root1=(-b+cmath.sqrt(descriminant))/2*a
    root2=(-b-cmath.sqrt(descriminant))/2*a
    return root1,root2
def main():
    print("求解二次方程 ax^2 + bx + c = 0")
    #获取用户输入
    a=get_float_input("请输入二次项系数 a（a ≠ 0）：")
    while a==0:
        print("二次方程的二次项系数 a 不能为 0！")
        a = get_float_input("请重新输入二次项系数 a（a ≠ 0）：")
    b=get_float_input("请输入一次项系数 b：")
    c=get_float_input("请输入常数项c：")
    root1,root2=solve_quadratic(a,b,c)
    print(f"方程的解为{root1}和{root2}")

if __name__=="__main__":
    main()

import math
import cmath
def input(a,b,c):
    if a==0:
        if b==0:
            return "无解" if c!=0 else "方程有无穷多个解"
        return f"方程是线性方程，解为x={-c/b}"
    delta=b**2-4*a*c
    if delta>0:
        root1=(-b+math.sqrt(delta))/2*a
        root2=(-b-math.sqrt(delta))/2*a
        return f"方程有两个实数根，x1={root1},x2={root2}"
    elif delta==0:
        root=-b/(2*a)
        return f"方程有个双重实数根，x={root}"
    else:
        root1 = (-b+cmath.sqrt(delta)) / 2 * a
        root2 = (-b-cmath.sqrt(delta)) / 2 * a
        return f"方程有两个复数根，x1={root1},x2={root2}"
a,b,c=1,-3,2
result=input(a,b,c)
print(result)

#4.计算三角形面积
#海伦公式，给定边长a,b,c。面积S=(s*(s-a)*(s-b)*(s-c))**0.5。s=（a+b+c)/2(三角形半周长）
import math
a=float(input("输入三角形第一边长："))
b=float(input("输入三角形第二边长："))
c=float(input("输入三角形第三边长："))
s=(a+b+c)/2
num_S=s*(s-a)*(s-b)*(s-c)
S=math.sqrt(num_S)
print(f"三角形的面试为{S}")

#5.摄氏温度转华氏温度
celsius=float(input("输入摄氏温度："))
fahrenheit=(celsius*1.8)+32
print("{0}的华氏温度为{1:.2f}".format(celsius,fahrenheit))

#6.使用 if...elif...else 语句判断数字是正数、负数或零：
num=float(input("输入一个数字："))
if num>0:
    print(f"{num}为正数")
elif num==0:
    print(f"{num}为零")
else:
    print(f"{num}为负数")

#7.判断输入的字符串是不是数字
num=input("输入一个数字：")
print(num.isnumeric())
#判断一个数字是否为奇数或偶数
num=int(input("输入一个数字："))
if num%2==0:
    print("{0}是偶数".format(num))
else:
    print("{}是奇数".format(num))

#8.判断用户输入的年份是否为闰年：如果年份能被 4 整除但不能被 100 整除，则是闰年。如果年份能被 400 整除，则也是闰年。
#实例一：
year=int(input("输入年份："))
if (year%4)==0:
    if (year%100)==0:
        if (year%400)==0:
            print(f"{year}是闰年")
        else:
            print(f"{year}不是闰年")
    else:
        print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")
#实例二：
def is_leap_year(year)：
    if (year%4==0 and year%100!=0) or (year%400==0):
        return Ture
    else:
        return False
year=2024
if is_leap_year(year):
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")

#9.质数判断
num=int(input("请输入一个数字："))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print("{0}不是质数".format(num))
            print(i,"乘",num//i,num)
            break
    else:  #for循环执行完毕，不满足if条件语句的即是质数。
            print("{0}是质数".format(num))
else:
    print("{0}不是质数".format(num))

#10.整数的阶乘
num=int(input("请输入一个数字："))
factorial=1
if num<0:
    print("负数没有阶乘")
elif num==0:
    print("0的阶乘为1")
else:
    for n in range(1,num+1):
        factorial=factorial*n
    print("{}的阶乘为{}".format(num,factorial))

#11.九九乘法表
for i in range(1,10):#当i=1时，j=1，输出1*1=1【range(1,2),2不取】
    for j in range(1,i+1):
        print("{}*{}={}\t".format(i,j,i*j),end="")
    print()  #一次内循环结束，准备换行输出

#12.斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。
nterms=int(input("你需要几项:"))
n1=0
n2=1
count=2 #计数
if nterms<=0:
    print("输入一个正整数！")
elif nterms==0:
    print("Fibonacci sequence:")
    print(n2)
else:
    print("Fibonacci sequence:")
    print(n1,",",n2,end=",")
    while count<nterms:
        nth=n1+n2
        print(nth,end=",")
        n1,n2=n2,nth #更新赋值
        count+=1

#13.阿姆斯特朗数.如果一个 n 位正整数等于其各位数字的 n 次方之和，则称该数为阿姆斯特朗数。 例如 1^3 + 5^3 + 3^3 = 153
#检测是否为阿姆斯特朗数
num=int(input("请输入一个数字"))
sum=0
n=len(str(num))
temp=num #一个中间变量temp,来计算正整数个位数
while temp>0:
    digit=temp%10 #个位数=除10取余
    sum+=digit**n #验证公式
    temp//=10 #去除个位数之后，剩下的正整数
if sum==num:
    print(f"{num}是阿姆斯特朗数")
else:
    print(f"{num}不是阿姆斯特朗数")
#在指定范围内print阿姆斯特朗数,指定范围用for x in range(范围)
lower=int(input("最小值："))
upper=int(input("最大值："))
for num in range(lower,upper+1):
    n = len(str(num))
    sum=0
    temp = num
    while temp > 0:
        digit = temp % 10  # 个位数=除10取余
        sum+=digit**n  # 验证公式
        temp //= 10  # 去除个位数之后，剩下的正整数
    if sum == num:
        print(num,end=" ")

#14.十进制转二进制、八进制、十六进制
dec=int(input("请输入数字：")) #十进制 decimal
print("十进制数为：",dec)
print("十进制转二进制：",bin(dec)) #二进制 binary
print("十进制转八进制：",oct(dec)) #八进制 octal
print("十进制转十六进制：",hex(dec)) #十六进制 hexadecimal
binary_number = '101010'
decimal_number = int(binary_number, 2)  # 二进制转换为十进制

#15.以下代码用于实现ASCII码与字符相互转换：
c = input("请输入一个字符: ")
# 用户输入ASCII码，并将输入的数字转为整型
a = int(input("请输入一个ASCII码: "))
print(c + " 的ASCII 码为", ord(c)) #单字符
print(a, " 对应的字符为", chr(a))

#16.以下代码用于实现最大公约数算法：
def gcd(x,y): #定义一个计算最大公约数的函数：
    x,y=abs(x),abs(y) # 取绝对值，避免负数计算错误
    if x==0 and y==0:  #理两数均为0的特殊情况
        raise ValueError
    elif x>y: #判断最小值
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if ((x%i==0)and(24%i==0)):
            gcd=i #循环计算公约数，每次都重新赋值给gcd
    return gcd #循环结束，最终留下最大的公约数
num1=int(input("输入第一个数字："))
num2=int(input("输入第二个数字："))
#设置检查模块并调用函数
try:
    print("{0}和{1}的最大公约数为{2}".format(num1,num2,gcd(num1,num2)))
except ValueError as e:
    print(e)

#17.以下代码用于实现最小公倍数算法：
def lcm(x, y):
    if x>y: #获取最大值
        greater=x
    else:
        greater=y
    while(True):
        if (greater%x==0)and(greater%y==0): #greater与x,y相等时，达成除x,y取余均为0，则为最小公倍数。
            lcm=greater #赋值给lcm
            break #达成条件的话跳出循环
        greater+=1
    return lcm #返回最小公倍数
num1=int(input("输入第一个数："))
num2=int(input("输入第二个数："))
print(f"{num1}和{num2}的最小公倍数为{lcm(num1,num2)}") #格式化字符串以f开头，它会将变量或表达式计算后的值替换进去。

#18.以下代码用于生成指定日期的日历：
import calendar #导入日历模块
yy=int(input("请输入年份："))
mm=int(input("请输入月份："))
print(calendar.month(yy,mm))
#18.以下代码使用递归的方式来生成斐波那契数列：
def recur_fibo(n):
    if n<=1:return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
nterms=int(input("您要几项"))
if nterms<0:print("请输入正数")
else:
    print("斐波那契数列：")
    for i in range(nterms):
        print(recur_fibo(i)) #用for循环，依次输出每一项。

#19.写文件，读文件
with open("测试.txt","wt") as outfile:
    outfile.write("这个文档中会写入这句话\n记住要自己输入换行符")
with open("测试.txt","rt") as infile:
    test=infile.read()
print(test)

#20.判断字符串
str="python3"
print(str.isalnum()) #判断字符串是否都是数字或者字母
print(str.isalpha()) #判断字符串是否都是字母
print(str.isdigit()) #判断字符串是否都是数字
print(str.islower()) #判断字符串是否都是小写字母
print(str.isupper()) #判断字符串是否都是大写字母
print(str.istitle()) #判断字符串是否都是首字母大写，其他小写
print(str.isspace()) #判断字符串是否都是空白字符
str2="have fun"
print(str2.upper())   # 把所有字符中的小写字母转换成大写字母
print(str2.lower())   # 把所有字符中的大写字母转换成小写字母
print(str2.capitalize())  # 把第一个字母转化为大写字母，其余小写
print(str2.title())   # 把每个单词的第一个字母转化为大写，其余小写

#21.获取昨天的日期
import datetime
def getyesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    yesterday=today-oneday
    return yesterday
print(getyesterday())

#22.list常用操作
li=["1","2","5","7","apple","banana"]
print(li[0])
print(li[:])
print(li[-2]) #负数索引
print(li[1:-1])
print(li[0:3])
print(li[:5])
print(li[-2:])
li.append("8")
li.insert(2,"3")
li.extend(["egg","10","7"])
print(li)
li.remove("7") #删除首次出现的值
print(li.pop()) #返回删除的最后一个元素
print(li)
s="".join(li) #join只能用于元素是字符串的 list;
print(s)
print(s.split("//")) #split将字符串分割成多个list元素，split接受一个可选的第二个参数, 它是要分割的次数。

#23.约瑟夫生者死者小游戏
#30个人在一条船上，超载，需要 15 人下船。于是人们排成一队，排队的位置即为他们的编号。报数，从 1 开始，数到 9 的人下船。如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？
people={} #创建一个字典，key表示在船上的三十个人。
for x in range(1,31): #表示三十个人，每个人有一个编号。
    people[x]=1 #value=1，表示人在船上，在people字典里。
#print(people) #打印验证
check=0 #报数计数器
i=1 #人员编号
j=0 #符合要求的人，即下船的人
#思考逻辑：for循环设置30个编号，放到字典或者列表里备用。需要一个变量j来表示下船的人，到达15，跳出游戏循环。需要一个变量作为报数检测，到9下船，下一位重复。
while i<=31:
    if i==31:
        i=1 #报数到31号的时候，重置为1，循环条件。
    elif j==15:
        break #控制条件，到15个人之后就停止
    else:
        if people[i]==0:
            i+=1
            continue #当value=0时，表示该编号人员已下船，跳过。
        else:
            check+=1 #报数
            if check==9:
                people[i]=0 #修改value为0，代表已下船
                check=0 #重新报数
                print(f"{i}号下船了")
                j+=1 #下船人数+1
            else:
                i+=1 #不满足check条件的，继续循环
                continue

#24.n个自然数的立方和
def sumOfSeries(n):
    sum=0
    for i in range(1,n+1):
        sum+=i**3
    return sum
print(sumOfSeries(5))

#25.计算数组元素之和
#定义数组array
def _sum(arr):
    return sum(arr)
arr=[1,2,3,4]
print(_sum(arr))

#26.数组翻转指定个数的元素，(ar[],d,n)将长度为n的数组arr的前面d个元素翻转到数组尾部。
#实例一
def leftRotate(arr, d, n): #定义一个函数，可以接受三个函数，arr数组，d旋转的次数，n数组的长度
    for i in range(d): #调用下面这个函数d次,就是旋转d次
        leftRotatebyOne(arr, n)
def leftRotatebyOne(arr, n): #定义一个函数，接受两个参数，arr数组，n数组的长度
    temp = arr[0] #数组的第一个数临时赋值给temp
    for i in range(n-1):
        arr[i] = arr[i+1] #用for循环，将数据往左移动一个位置
    arr[n-1] = temp #将temp赋值给最后一个位置，完成一次向左旋转，数组前面的第一位数换到最后
def printArray(arr,size): #定义一个函数打印函数，接收参数是打印的数组arr,size数组长度
    for i in range(size): #依次打印出7位数组
        print ("%d"% arr[i],end=" ")
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2, 7) #调用函数
printArray(arr, 7) #调用函数
#实例二
def leftRotate(arr,d,n):
    for i in range(gcd(d, n)): #(避免左旋周期性操作，采取旋转次数和数组长度最大公约数作为旋转次数)
        temp = arr[i]  #当循环开始时，保存初始变量到temp
        j = i #用j来跟踪位置变动
        while 1:
            k = j + d #新索引k=当前位置j+旋转次数d
            if k >= n: #当新索引超出或数组长度
                k = k - n #让新索引回归正确位置
            if k == i: #当新索引等于初始位置，相当于移动到初始位置时，则已完成旋转，跳出
                break
            arr[j] = arr[k] #每次旋转时，交换位置，相当于移动一位
            j = k #然后更新当前位置索引为最新索引，继续循环
        arr[j] = temp #将初始位置放置到最终位置
def printArray(arr, size):
    for i in range(size):
        print("%d" % arr[i], end=" ")
def gcd(a, b): #定义一个最大公约数函数（递归函数）
    if b == 0:
        return a;
    else:
        return gcd(b, a%b)

arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2, 7)
printArray(arr, 7)
#案例三（思考逻辑：通过交换三次位置，来达成旋转的目的）
def rverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end - 1
def leftRotate(arr, d):
    n = len(arr)
    rverseArray(arr, 0, d - 1)
    rverseArray(arr, d, n - 1)
    rverseArray(arr, 0, n - 1)
def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i], end=' ')
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2)
printArray(arr)

#27.将列表中的头尾两个元素对调
#实例一：
def swapList(newList):
    size = len(newList) #获取长度
    temp = newList[0] #暂存首位数
    newList[0] = newList[size - 1] #将末尾数赋值给首个位置
    newList[size - 1] = temp #将暂存的首位数赋值给末尾数
    return newList #返回新的list
newList = [1, 2, 3]
print(swapList(newList))
#实例二
def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0] #赋值交换位置
    return newList
newList = [1, 2, 3]
print(swapList(newList))

#28.将列表中的指定位置的两个元素对调
#实例一
def swapPositions(list, pos1, pos2): #定义一个函数，接受3个参数，列表，指定位置1,指定位置2
    list[pos1], list[pos2] = list[pos2], list[pos1] #交换位置
    return list
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(swapPositions(List, pos1 - 1, pos2 - 1))
#实例二
def swapPositions(list, pos1, pos2):
    first_ele = list.pop(pos1) #删除并返回第一个位置的数
    second_ele = list.pop(pos2 - 1) #删除并返回第二个位置的数
    list.insert(pos1, second_ele) #插入第一个数到第二个位置
    list.insert(pos2, first_ele)
    return list
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(swapPositions(List, pos1 - 1, pos2 - 1)) #调用函数
#实例三
def swapPositions(list, pos1, pos2):
    get = list[pos1], list[pos2] #将两个数据暂存赋值给get
    list[pos2], list[pos1] = get #用一个中间数完成位置的调换
    return list
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(swapPositions(List, pos1 - 1, pos2 - 1))

#29.定义一个列表，并将它翻转。
#实例一
def Reverse(lst):
    return [ele for ele in reversed(lst)]  #reversed返回一个迭代器，可以反转列表元素字符串
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))
#实例二
def Reverse(lst):
    lst.reverse() #reverse是列表的一个方法，可以直接修改原列表
    return lst
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))
#实例三
def Reverse(lst):
    new_lst = lst[::-1] #用切片反转列表
    return new_lst
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

#30.判断元素是否在列表中存在
test_list_set = [1, 6, 3, 5, 3, 4]
test_list_bisect = [1, 6, 3, 5, 3, 4]
print("查看 4 是否在列表中 ( 使用 set() + in) : ")
test_list_set = set(test_list_set)
if 4 in test_list_set: #变为集合，集合中的元素唯一，用in
    print("存在")
print("查看 4 是否在列表中 ( 使用 count()) : ")
if test_list_bisect.count(4) > 0: #用列表中的count计数，大于0，则表示存在
    print("存在")

#31.移除列表中重复的元素
#实例一：用集合set
list_1 = [1, 2, 1, 4, 6]
print(list(set(list_1)))
#实例二：使用辅助集合保持顺序地去重
def remove_duplicates(lst): #定义一个副本函数
    seen = set() #设立一个空集合，目的是为了装已见过的元素
    unique_list = [] #设立一个空集合
    for item in lst: #用for循环遍历list
        if item not in seen: #判断list的元素在不在空集合，不在的话，加入空集合。在的话，不操作，去重。
            seen.add(item)
            unique_list.append(item) #然后直接放入list
    return unique_list #最终返回一个list
# 示例
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(original_list)
print(unique_list)
#实例三：dict.fromkeys() 方法也可以用于去重并保持顺序
def remove_duplicates(lst):
    return list(dict.fromkeys(lst)) #字典的键是唯一的
# 示例
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(original_list)
print(unique_list)
#实例四：列表推导式结合条件判断也可以实现去重功能。
def remove_duplicates(lst):
    unique_list = []
    [unique_list.append(item) for item in lst if item not in unique_list]
    return unique_list
# 示例
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(original_list)
print(unique_list)

#32.定义一个列表，并将该列表元素复制到另外一个列表上。
#实例一
def clone_l(li1):
    copy_li=li1[:]
    return copy_li
li1=[1,2,3,4,5]
li2=clone_l(li1)
print(f"原列表{li1}")
print(f"复制后的列表{li2}")
#实例二: 使用 extend() 方法
def clone_l(li1):
    copy_li=[]
    copy_li.extend(li1)
    return copy_li
li1=[1,2,3,4,5]
li2=clone_l(li1)
print(f"原列表{li1}")
print(f"复制后的列表{li2}")
#实例三：使用 list() 方法
def clone_l(li1):
    copy_li=list(li1)
    return copy_li
li1=[1,2,3,4,5]
li2=clone_l(li1)
print(f"原列表{li1}")
print(f"复制后的列表{li2}")

#33.计算元素在列表中出现的次数
def countX(lst,x):
    count=0
    for ele in lst:
        if ele==x:
            count+=1
    return count
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print(countX(lst, x))

#34.定义一个数字列表，并计算列表元素之和。
#实例一
total=0
list=[1,2,3,4,5]
for ele in range(0,len(list)):
    total=total+list[ele]
print(f"列表元素之和：{total}")
#实例二：使用 while() 循环
list=[1,2,3,4,5]
total=0
ele=0
while (ele<len(list)):
    total=total+list[ele]
    ele+=1
print("列表元素之和为: ", total)
#实例三：使用递归
list1=[1,2,3,4,5]
def sumOfList(list, size):
    if (size == 0):
        return 0
    else:
        return lsist[size - 1] + sumOfList(list, size - 1)
total = sumOfList(list1, len(list1))
print("列表元素之和为: ", total)

#35.计算列表元素之积
def multiplyList(mylist):
    result=1
    for i in mylist:
        result=result*i
    return result
list1=[1,5,6]
print("列表元素之积：",multiplyList(list1))

#36.查找列表中最小/大元素
#查找最小元素
list1 = [10, 20, 4, 45, 99]
list1.sort() #方法一：排序，默认升序reverse=False
print("最小元素为:", *list1[:1]) #输出排序后的第一个元素即为最小元素,*用于解包列表，直接输出元素，而不是列表
list1 = [10, 20, 4, 45, 99] #方法二，使用内置函数min
print("最小元素为:",min(list1))
#查找最大元素
print("最小元素为:", list1[-1]) #输出最末元素即为最大元素,*用于解包列表，直接输出元素，而不是列表
print("最小元素为:",max(list1)) #使用max

#37.移除字符串中的指定位置字符
Str="Hello，World!"
New_str=""
for i in range(0,len(Str)):
    if i!=2:
        New_str+=Str[i]
print("移除第三个字符后的字符串为：",New_str)

#38.判断字符串是否存在子字符串
def checkstr(string,sub_str):
    if string.find(sub_str)==-1:
        print("不存在") #str.find()判断是否包含子字符串，不包含则返回-1。包含则返回索引值
    else:
        print("存在")
string="May loves China!"
sub_str="love"
checkstr(string,sub_str)

#39.字符串长度
str="May loves 咚咚"
print(len(str)) #用内置函数len判断字符串长度
def findlen(str):
    counter=0
    while str[counter:]: #字符串切片，当counter长度超过str,返回空字符串
        counter+=1
    return counter
print(findlen(str))

#40.使用正则表达式提取字符串中的 URL
import re
def Find(string):
    # findall() 查找匹配正则表达式的字符串
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)   #直接匹配百分号字符 %，常用于标识 URL 编码的起始字符（如 %20 表示空格）
    return url
string = '小红书的网页地址为：https://www.xiaohongshu.com，Google 的网页地址为：https://www.google.com'
print("Urls: ", Find(string))

#41.给定一个字符串代码，然后使用 exec() 来执行字符串代码。
def exec_code(): #获取一段代码，以字符串的形式输入，用exec()python内置函数，来执行。
    LOC = "
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact = fact*i
    return fact
print(factorial(5))
"
    exec(LOC)
exec_code()

#42.字符串翻转
Str="？nohtyp evoL yaM"
print(Str[::-1]) #使用切片翻转
print("".join(reversed(Str))) #reversed生成器,生成单个字符，用join连接字符。

#43.给定一个字符串，从头部或尾部截取指定数量的字符串，然后将其翻转拼接。
def rotate(inputstr,d): #定义一个函数，接受两个参数，inputstr输入的字符串，d指定的字符串。
    Lfirst=inputstr[0:d] #从左边截取第一个字符串
    Lsecond=inputstr[d:] #左截取第二个字符串
    Rfirst=inputstr[0:len(inputstr)-d]  #右边截取第一个字符串
    Rsecond=inputstr[len(inputstr)-d:]
    print("头部切片翻转: ", (Lsecond+Lfirst))
    print("尾部切片翻转: ", (Rsecond+Rfirst))
if __name__ == "__main__":
    input = '123456'
    d = 2  # 截取两个字符
    rotate(input, d)

#44.给定一个字典，然后按键(key)或值(value)对字典进行排序。
#实例一：用列表sort
def dictionairy():
    key_value = {} # 声明字典
    key_value[2] = 56 #初始化，添加键值
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
    print("按键(key)排序:")
    for i in sorted(key_value): # sorted(key_value) 返回重新排序的列表      # 字典按键排序
        print((i, key_value[i]), end=" ")
def main():
    dictionairy() # 调用函数
if __name__ == "__main__": # 主函数
    main()
#实例二：按值(value)排序
def dictionairy():
    key_value = {} # 声明字典
    key_value[2] = 56  # 初始化
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
    print("按值(value)排序:")
    print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))) #将字典按指定key来排序，kv[1]是值，kv[0]是键。值相同时按键大小排。
def main():
    dictionairy()
if __name__ == "__main__":
    main()
#实例三：字典列表排序
lis = [{"name": "Taobao", "age": 100},
       {"name": "Runoob", "age": 7},
       {"name": "Google", "age": 100},
       {"name": "Wiki", "age": 200}]
# 通过 age 升序排序
print("列表通过 age 升序排序: ")
print(sorted(lis, key=lambda i: i['age']))
print("\r") #换行
# 先按 age 排序，再按 name 排序
print("列表通过 age 和 name 排序: ")
print(sorted(lis, key=lambda i: (i['age'], i['name'])))
print("\r")
# 按 age 降序排序
print("列表通过 age 降序排序: ")
print(sorted(lis, key=lambda i: i['age'], reverse=True))

#45.计算字典值之和
def returnSum(myDict): #定义一个函数，接受一个参数
    sum = 0
    for i in myDict: #i是key,mydict[i]是value
        sum = sum + myDict[i]
    return sum
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))

#46.移除字典点键值(key/value)对
#实例一:使用del移除
test_dict = {"spring":1,"summer":2,"autumn":3,"winter":4}
# 输出原始的字典
print("字典移除前:",str(test_dict))
# 使用del移除winter
del test_dict['winter']
# 输出移除后的字典
print("字典移除后:"+str(test_dict)) #当需要输出一段包含变量值的文本时，可以使用+号将文本字符串和变量值（转换为字符串后）连接起来.
#移除没有的 key 会报错
#del test_dict['beauty']
#实例二：使用pop移除
removed_value=test_dict.pop('autumn') # 使用pop移除autumn,pop返回的是移除的元素的value
print("移除的key对应的value为:"+str(removed_value))
print("字典移除后:"+str(test_dict))
removed_value=test_dict.pop('Baidu','没有该键(key)')#使用pop()移除没有的key不会发生异常,我们可以自定义提示信息.
print("字典移除后:"+str(test_dict))
print("移除的值为:"+str(removed_value))
#实例三：使用items()移除,字典推导式
new_dict={key:val for key,val in test_dict.items() if key!='spring'} #相当于创建一个新字典，字典里不包含spring
print("字典移除后:"+str(new_dict))

#47.合并字典
#实例一：使用update()方法，第二个参数合并第一个参数
def Merge(dict1, dict2):
    return (dict2.update(dict1))
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
print(Merge(dict1, dict2)) #merge不能直接合并字典
print(dict2) #dict2合并了dict1
#实例二：使用**，函数将参数以字典的形式导入
def Merge2(dict1, dict2):
    res={**dict1, **dict2} #使用**运算符将字典解包为关键字参数
    return res
dict3 = Merge2(dict1, dict2)
print(dict3)
#从Python 3.9开始，引入了|运算符来合并字典。这个运算符会创建一个新的字典，包含所有键，但值会是后一个字典中对应键的值（如果有重复键的话）。
dict4={'d': 6, 'c': 4, 'a': 20}  # 注意这里'a'键是重复的
merged_dict=dict1|dict4
print(merged_dict)

#48.将字符串的时间转换为时间戳(时间戳是一个很大的数字，代表从1970年1月1日到现在的秒数）
import time
a1="2019-5-10 23:40:00"
timeArray=time.strptime(a1,"%Y-%m-%d %H:%M:%S") #step1把字符串时间变成python理解的时间数组
timeStamp=int(time.mktime(timeArray)) #step2转换为时间戳
print(timeStamp)
# 时间格式转换 - 转为 /
a2 = "2019/5/10 23:40:00"
timeArray=time.strptime(a2, "%Y/%m/%d %H:%M:%S") # 先转换为时间数组,然后转换为其他格式
otherStyleTime=time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
print(otherStyleTime)

#49.获取几天前的时间
#实例一：计算几天前的时间并转换为指定格式
import time
import datetime
# 先获得时间数组格式的日期
threeDayAgo=(datetime.datetime.now()-datetime.timedelta(days=3))
# 转换为时间戳
timeStamp = int(time.mktime(threeDayAgo.timetuple())) #把时间转换成元祖格式的时间数组才能完成时间戳的计算
# 转换为其他字符串格式
otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)
#实例二：
import time
import datetime
# 给定时间戳
timeStamp=1557502800
dateArray=datetime.datetime.utcfromtimestamp(timeStamp) #得到时间戳对应的时间
threeDayAgo=dateArray-datetime.timedelta(days=3) #计算此日期三天前的时间
print(threeDayAgo)

#50.将时间戳转换为指定格式日期
#实例一：
import time
now=int(time.time()) # 获得当前时间时间戳
# 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
timeArray = time.localtime(now) #将时间戳转换为时间
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)
#实例二：
import datetime
now = datetime.datetime.now() # 获得当前时间
# 转换为指定的格式
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)
#实例三：指定时间戳
import time
timeStamp = 1557502800
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)
#实例四：
import datetime
timeStamp = 1557502800
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)

#51.通过对 26 个字母的设定，设置自己要输出的字体。
name="May"
length=len(name)
for x in range(0,length):
    c=name[x]
    c=c.upper()
    if (c == "A"):
        print("....AA....\n..A....A..\n..AAAAAA..", end=" ")
        print("\n..A....A..\n..A....A..\n\n")
    elif (c == "B"):
        print("..######..\n..#....#..\n..#####...", end=" ")
        print("\n..#....#..\n..######..\n\n")
    elif (c == "C"):
        print("..######..\n..#.......\n..#.......", end=" ")
        print("\n..#.......\n..######..\n\n")
    elif (c == "D"):
        print("..#####...\n..#....#..\n..#....#..", end=" ")
        print("\n..#....#..\n..#####...\n\n")
    elif (c == "E"):
        print("..######..\n..#.......\n..#####...", end=" ")
        print("\n..#.......\n..######..\n\n")
    elif (c == "F"):
        print("..######..\n..#.......\n..#####...", end=" ")
        print("\n..#.......\n..#.......\n\n")
    elif (c == "G"):
        print("..######..\n..#.......\n..#.####..", end=" ")
        print("\n..#....#..\n..#####...\n\n")
    elif (c == "H"):
        print("..#....#..\n..#....#..\n..######..", end=" ")
        print("\n..#....#..\n..#....#..\n\n")
    elif (c == "I"):
        print("..######..\n....##....\n....##....", end=" ")
        print("\n....##....\n..######..\n\n")
    elif (c == "J"):
        print("..######..\n....##....\n....##....", end=" ")
        print("\n..#.##....\n..####....\n\n")
    elif (c == "K"):
        print("..#...#...\n..#..#....\n..##......", end=" ")
        print("\n..#..#....\n..#...#...\n\n")
    elif (c == "L"):
        print("..#.......\n..#.......\n..#.......", end=" ")
        print("\n..#.......\n..######..\n\n")
    elif (c == "M"):
        print("..M....M..\n..MM..MM..\n..M.MM.M..", end=" ")
        print("\n..M....M..\n..M....M..\n\n")
    elif (c == "N"):
        print("..#....#..\n..##...#..\n..#.#..#..", end=" ")
        print("\n..#..#.#..\n..#...##..\n\n")
    elif (c == "O"):
        print("..######..\n..#....#..\n..#....#..", end=" ")
        print("\n..#....#..\n..######..\n\n")
    elif (c == "P"):
        print("..######..\n..#....#..\n..######..", end=" ")
        print("\n..#.......\n..#.......\n\n")
    elif (c == "Q"):
        print("..######..\n..#....#..\n..#.#..#..", end=" ")
        print("\n..#..#.#..\n..######..\n\n")
    elif (c == "R"):
        print("..######..\n..#....#..\n..#.##...", end=" ")
        print("\n..#...#...\n..#....#..\n\n")
    elif (c == "S"):
        print("..######..\n..#.......\n..######..", end=" ")
        print("\n.......#..\n..######..\n\n")
    elif (c == "T"):
        print("..######..\n....##....\n....##....", end=" ")
        print("\n....##....\n....##....\n\n")
    elif (c == "U"):
        print("..#....#..\n..#....#..\n..#....#..", end=" ")
        print("\n..#....#..\n..######..\n\n")
    elif (c == "V"):
        print("..#....#..\n..#....#..\n..#....#..", end=" ")
        print("\n...#..#...\n....##....\n\n")
    elif (c == "W"):
        print("..#....#..\n..#....#..\n..#.##.#..", end=" ")
        print("\n..##..##..\n..#....#..\n\n")
    elif (c == "X"):
        print("..#....#..\n...#..#...\n....##....", end=" ")
        print("\n...#..#...\n..#....#..\n\n")
    elif (c == "Y"):
        print("..Y....Y..\n...Y..Y...\n....YY....", end=" ")
        print("\n....YY....\n....YY....\n\n")
    elif (c == "Z"):
        print("..######..\n......#...\n.....#....", end=" ")
        print("\n....#.....\n..######..\n\n")
    elif (c == " "):
        print("..........\n..........\n..........", end=" ")
        print("\n..........\n\n")
    elif (c == "."):
        print("----..----\n\n")

#52.二分查找：返回 x 在 arr 中的索引，如果不存在返回 -1
def binarySearch(arr, l, r, x): #定义一个函数，接受四个参数arr数组，l起始查询索引，r数组长度，x查找的数字
    # 基本判断
    if r >= l:  #数组长度大于起始索引的话
        mid = int(l + (r - l) / 2) #中间数=起始索引+（数组长度-起始索引）/2
        # 元素整好的中间位置
        if arr[mid] == x:
            return mid
            # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
            # 元素大于中间位置的元素，只需要再比较右边的元素
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1   # 不存在
# 测试数组
arr = [2, 3, 4, 10, 40]
x = 10
# 函数调用
result = binarySearch(arr, 0, len(arr) - 1, x)
if result != -1:
    print("元素在数组中的索引为 %d" % result)
else:
    print("元素不在数组中")

#53.线性查找:按一定的顺序检查数组中每一个元素，直到找到所要寻找的特定值为止.
def search(arr,n,x):
    for i in range(0,n):
        if arr[i]==x:
            return i
    return -1
# 在数组 arr 中查找字符 D
arr = [ 'A', 'B', 'C', 'D', 'E' ]
x = 'D'
n = len(arr)
result = search(arr, n, x)
if(result == -1):
    print("元素不在数组中")
else:
    print("元素在数组中的索引为", result)

#54.插入排序
def insertionSort(arr):
    for i in range(1, len(arr)): #从第二个数开始
        key = arr[i] #将当前要插入的元素保存到key变量中，后续会用它来比较和插入
        j = i - 1 #初始化j为当前元素的前一个位置
        while j >= 0 and key < arr[j]: #当前元素比已排序元素小时才需要移动
            arr[j + 1] = arr[j] #将比key大的元素向后移动一位
            j -= 1 #继续往前比较，直到找到key应该插入的位置
        #当j不满足while循环条件时，退出循环，则key的位置就在arr[j+1]
        arr[j + 1] = key #把key放到它应该在的位置
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print("排序后的数组:")
for i in range(len(arr)):
    print("%d"% arr[i],end=",")

#55.快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，然后递归地排序两个子序列。
#先分割，然后排序.arr[]-->排序数组;low-->起始索引;high-->结束索引。
def partition(arr, low, high):
    i=(low-1) #初始化一个变量i,表示小于或等于基准值的元素的索引，初始值为low-1
    pivot=arr[high] #将数组最后一个位置的数作为基准值
    for j in range(low, high): #从low到high-1遍历数组
        if arr[j] <= pivot: # 当前元素小于或等于 pivot 时
            i = i + 1 #表示找到了一个新的小于或等于基准值的元素
            arr[i], arr[j] = arr[j], arr[i] #交换位置，将小于或等于基准值的元素移到左边
    arr[i + 1], arr[high] = arr[high], arr[i + 1] #将基准值放到正确的位置上，即左边都是小于或等于它的，右边都是大于它的。
    return (i + 1) #返回基准值的最终索引
# 快速排序函数
def quickSort(arr, low, high): #定义了一个名为quickSort的函数，用于递归地对数组进行快速排序。
    if low < high: #如果low小于high，说明还有数据需要排序。
        pi=partition(arr, low, high) #调用partition函数进行分区，得到基准值的索引pi
        quickSort(arr, low, pi-1) #递归地对基准值左边的数组进行排序
        quickSort(arr, pi+1, high) #右边
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("排序后的数组:")
for i in range(n): #遍历排序后的数组
    print("%d" % arr[i],end=",")

#56.选择排序
#首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
A = [64, 25, 12, 22, 11]
for i in range(len(A)):
    min_idx=i #用min_idx表示当前i的位置，假设它最小
    for j in range(i+1, len(A)): #遍历的剩下元素
        if A[min_idx]>A[j]: #如果满足i位置上的元素>j位置上的
            min_idx=j #则j为最小元素位置
    A[i], A[min_idx] = A[min_idx], A[i] #把新的最小元素和当前i换位置，继续下一轮
print("排序后的数组：")
for i in range(len(A)):
    print("%d" % A[i],end=",")

#57.冒泡排序（Bubble Sort）：它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
def bubbleSort(arr):
    n=len(arr)
    # 遍历所有数组元素
    for i in range(n): #循环n次,索引从0开始，到n-1
        # Last i elements are already in place
        for j in range(0, n-i-1): #内循环n-1-i,不去循环已经完成排序的元素
            if arr[j] > arr[j+1]: #比较前后两个元素，如果前面的大于后面的
                arr[j], arr[j+1] = arr[j+1], arr[j] #交换位置，继续下次循环
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i],end=",")

#58.归并排序（mergesort）.分治法:分割:递归地把当前序列平均分割成两半。集成:在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）。
def merge(arr, l, m, r): #定义一个函数接受4个参数，合并两个有序的部分。l是起始下标，r是结束下标，m是中间位置下标。
    n1 = m-l+1 #左边数组的长度
    n2 = r-m #右边数组的长度
    # 创建两个临时数组
    L = [0]*(n1)
    R = [0]*(n2)
    # 拷贝数据到临时数组 arrays L[]和R[]
    for i in range(0, n1):
        L[i] = arr[l+i]
    for j in range(0,n2):
        R[j] = arr[m+1+j]
        # 归并临时数组到 arr[l..r]
    i = 0  # 初始化第一个子数组的索引
    j = 0  # 初始化第二个子数组的索引
    k = l  # 初始归并子数组的索引
    while i<n1 and j<n2: #当i和j在长度范围内是循环
        if L[i] <= R[j]: #比较左右两边的元素，左边小于等于右边的元素
            arr[k] = L[i] #就把左边的元素放回数组
            i+=1 #每次满足此条件左边索引+1
        else: #当左边大于右边时
            arr[k] = R[j] #交换位置
            j+=1 #每次进行到这里右边索引+1继续
        k+=1 #每次循环归并数组的索引+
    # 拷贝 L[] 的保留元素
    while i<n1: #满足此条件的循环同时进行，如果右边已完成数组归并排序，则把左边的按顺序放回
        arr[k] = L[i]
        i+=1
        k+=1
    # 拷贝 R[] 的保留元素
    while j<n2:
        arr[k] = R[j]
        j+=1
        k+=1
def mergeSort(arr, l, r): #分割排序，通过不断‌二分数组，先递归排序子数组，再合并两个有序子数组，最终完成整体排序。
    if l<r:
        m = int((l+(r-1))/2) #找到中间点，分成左右两边
        mergeSort(arr, l, m) #递归地对左半部分和右半部分排序
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r) #把排好序的左右两半合并起来
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("给定的数组：")
for i in range(n):
    print("%d" % arr[i],end=",")
mergeSort(arr, 0, n-1) #调用函数
print("\n排序后的数组：")
for i in range(n):
    print("%d" % arr[i],end=",")

#59.堆排序（Heapsort）：堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。
def heapify(arr, n, i): #建堆函数。接收三个参数，arr数组，n数组长度，i是当前要调整的节点的位置。
    largest = i #我们先假设当前根节点i是最大元素位置，所以把largest设为i。
    l = 2*i + 1  # left = 2*i + 1 (索引从0开始左边节点的位置）
    r = 2*i + 2  # right = 2*i + 2
    if l<n and arr[i] < arr[l]: #左边节点索引小于数组长度，如果当前根节点元素小于它的左节点元素
        largest = l #则左节点作为最大位置
    if r<n and arr[largest] < arr[r]: #右节点索引小于数组长度，左最大元素节点小于右节点元素
        largest = r #则最大元素节点为右节点
    if largest!=i: #如果最大元素节点不是当前根节点
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换它俩的位置
        heapify(arr, n, largest) #递归的检查每一个新的根节点。
def heapSort(arr): #堆排序
    n = len(arr)
    # Build a maxheap.从数组的最后一个非叶子节点开始，向前遍历到第一个节点，对每个节点调用heapify函数，构建一个最大堆。
    for i in range(n, -1, -1): #从最后一个数开始，倒着逐个调用heapify函数，按此规则建立大根堆。
        heapify(arr, n, i)
        # 一个个交换数组元素
    for i in range(n-1, 0, -1): #从数组末尾向前遍历（n-1到1），i表示当前未排序部分的边界
        arr[i], arr[0] = arr[0], arr[i]  # 交换堆顶元素（arr[0]，即当前最大值）与未排序部分的最后一个元素（arr[i]）
        heapify(arr, i, 0) #对剩余未排序部分（arr[0:i]）重新执行堆化（heapify），从根节点0开始调整，确保新的堆顶是剩余元素中的最大值
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("排序后")
for i in range(n):
    print("%d" % arr[i])

#60.计数排序：计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中
def countSort(arr):
    output = [0 for i in range(256)] #创建长度为256的列表，初始化为0
    count = [0 for i in range(256)]
    ans = ["" for _ in arr] #创建与arr长度相同的列表 ans，所有元素初始化为空格。用来放排序后的结果
    for i in arr: #遍历arr，使用ord(i) 获取字符的ASCII值，并在count对应位置加 1
        count[ord(i)] += 1  #比如count(97)的位置上+1,表示有几个97。
    for i in range(256):
        count[i] += count[i-1] #遍历 count，count[i]就表示从第一个字符到当前字符的累积出现次数，确定字符在排序后的位置。
    for i in range(len(arr)): #再次遍历 arr，根据 count 中对应位置的值，将字符放入 output之后，count-1
        output[count[ord(arr[i])] - 1] = arr[i]
        count[ord(arr[i])] -= 1 #更新count
    for i in range(len(arr)): #遍历 output，将字符赋值给 ans 中对应位置，形成排序后的字符数组。
        ans[i] = output[i]
    return ans
arr = "wwwgithubcom"
ans = countSort(arr)
print("字符数组排序 %s" % ("".join(ans)))

#61.希尔排序，也称递减增量排序算法,是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法.
#先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序。
def shellSort(arr):
    n = len(arr) #获取数组长度，确定增量gap
    gap = n//2 #增量
    while gap > 0: #当增量=1之前一直循环
        for i in range(gap, n): #循环索引从gap开始到n-1
            temp = arr[i] #暂存，防止修改原数据
            j = i #把i赋值给变量j
            while j >= gap and arr[j-gap] > temp: #判断每组元素大小。当j>=gap，比较j和它前面的数的大小，如果逆序，则操作
                arr[j] = arr[j-gap] #则将arr[j-gap]往后移到arr[j]
                j -= gap #更新j的值
            arr[j] = temp #把暂存的temp放到前面,相当于交换位置，然后下一轮循环。
        gap = gap//2 #跳出for循环之后更新增量值，继续外循环。
arr = [12, 34, 54, 2, 3]
n = len(arr)
print("排序前:")
for i in range(n):
    print(arr[i],end="，")
shellSort(arr) #调用函数
print("\n排序后:")
for i in range(n):
    print(arr[i],end="，")

#62.拓扑排序：对一个有向无环图，进行拓扑排序。可以用来判断环，有环，拓扑排序进行不下去。
from collections import defaultdict #自动给不存在的键创建默认值（这里是空列表）
class Graph: #创建一个图类
    def __init__(self, vertices):  #定义类
        self.graph = defaultdict(list) #使用邻接表表示图，格式如{0: [1,2], 1: [3]}，表示顶点0指向1和2
        self.V = vertices #记录顶点数量
    def addEdge(self, u, v): #添加边的方法
        self.graph[u].append(v) #添加u→v的有向边
    def topologicalSortUtil(self, v, visited, stack): #拓扑排序的核心工具方法
        visited[v] = True #标记当前节点已访问
        for i in self.graph[v]: # 遍历所有邻接顶点
            if visited[i] == False: # 遇到未访问顶点则递归
                self.topologicalSortUtil(i, visited, stack)
        stack.insert(0, v) # 把当前节点插入结果列表的最前面
    def topologicalSort(self): #拓扑排序主方法
        visited = [False] * self.V # 创建访问记录表（初始都未访问）
        stack = [] # 准备结果容器
        for i in range(self.V): # 检查所有节点
            if visited[i] == False: # 确保每个连通分量都被处理
                self.topologicalSortUtil(i, visited, stack)
        print(stack) #输出拓扑序
g = Graph(6) # 创建6个节点的图
g.addEdge(5, 2); # 添加边表示依赖关系：添加5→2的边
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);
print("拓扑排序结果：")
g.topologicalSort()

#63.简单的银行系统
means = [0, 0, 0] # 资产数组：[存款，理财收益，负债]
loan = 0 # 贷款总额
rate = 0 # 贷款利率
pay = 0 # 每年还款额
investment = 0 # 每月定投金额
annual_rate = 0 # 年收益率
# 计算定投预期收益
# 定投收益的计算公式为：M=a(1+x)[-1+(1+x)^n]/x;(复利公式)
# 其中M代表预期收益，a代表每期定投金额，x代表收益率，而n代表定投期数。
# 假设用户每月定投金额为300元，一年也就是3600元，年收益率为15%，
# 定投期限为35年，则可以计算出收益为3600(1+15%)[-1+(1+15%)^35]/15%=3648044元。
def fixed_investment(inv, a_rate, y): #计算定期投资收益，inv月投资，a_rate收益率，y定投期限
    global means
    inv = 12 * inv #将月投资转为年投资（×12）
    a_rate = a_rate / 100 #收益率
    if a_rate == 0:
        expected = 0
    else:
        expected=inv*(1+a_rate)*(pow((1+a_rate),y)-1)/a_rate #计算预期收益
    print("定投的预期收入为:%.2f" % expected) #保留两位小数
    means[1] = expected #结果存入means[1]
    return expected
def balance(): #显示资产明细
    total = 0
    for i in means:
        total += i #计算总资产（存款+理财收益-负债）
    print("你的资产总额为：%.2f" % total)
    print("你的资产明细为：\n")
    print("存款：%.2f" % means[0])
    print("理财：%.2f" % means[1])
    print("负债：%.2f" % means[2])
def saving(amount): #存款
    global means
    if amount < 0:
        print("存款金额不可小于 0！")
    else:
        means[0] += amount
        print("已存款：%.2f 元" % amount)
        print("当前余额：%.2f 元" % means[0])
def draw_money(drawing): #取款
    global means
    if drawing < 0:
        print("取款金额不可小于 0！")
    elif drawing > means[0]:
        print("取款金额不可超过余额！")
    else:
        means[0]-=drawing
        print("已取款： %.2f 元" % drawing)
        print("当前余额： %.2f 元" % means[0])
def loans(loan, rate, pay, years): #贷款：模拟还款过程
    global means
    if pay < (loan-pay)*rate: #还款额<利息
        print("你是还不完的！！！")
    else:
        if years == 0: #不指定年限时计算还清年数
            count = 0
            while loan > 0:
                loan-=pay #贷款金额=原贷款金额-还款金额
                loan*=(1+rate) #贷款=贷款*(1+利率)
                count+=1 #每次还款后循环+1.直到还清贷款，即可计算还款年限。
            print("将在 %d 年后还完贷款。" % count)
        else:
            for _ in range(years): #指定年限时显示每年负债
                loan -= pay
                if loan == 0:
                    break
                else:
                    loan *= (1+rate)
                    print("你现在的负债是: %.2f" % loan)
            # means[2] = loan
            return loan
# 未来财务状况
def future(years): #综合计算未来资产
    income=fixed_investment(investment, annual_rate, years) #调用投资和贷款计算
    debt = loans(loan, rate, pay, years) #贷款即负债
    captial = means[0] + income - debt #资产=存款+投资收益-负债
    print("你第%i年的总资产有: %.3f" % (years, captial))
def init(): #显示菜单
    print('''以下为可办理的业务：
        1. 查询资产
        2. 存款
        3. 取款
        4. 计算复利
        5. 计算贷款
        6. 计算未来资产
        q. 退出''')
def main(): #交互式菜单
    init() #调用菜单
    while True:
        choice = input("请输入您要办理的业务代码: ")
        #  查询余额
        if choice == "1":
            balance()
        # 存款
        elif choice == "2":
            inc = float(input("请输入存款金额: "))
            saving(inc)
        # 取款
        elif choice == "3":
            dec = float(input("请输入取款金额: "))
            draw_money(dec)
        # 计算定投
        elif choice == "4":
            investment = float(input("请输入每月定投金额: "))
            annual_rate = float(input("请输入年收益率: "))
            years = int(input("请输入定投期限(年): "))
            if investment <= 0 or annual_rate <= 0 or years <= 0:
                print("输入的数据有误")
            else:
                money = fixed_investment(investment, annual_rate, years)
            print("最终收获: %.2f 元" % money)
        # 计算贷款
        elif choice == "5":
            loan = float(input("请输入当前贷款: "))
            rate = float(input("请输入年利率: "))
            pay = float(input("请输入每年还款: "))
            if loan <= 0 or rate <= 0 or pay <= 0:
                print("输入的数据有误")
            else:
                loans(loan, rate, pay, 0)
        elif choice == "6":
            years = int(input("希望查询多少年后的财务状况? "))
            future(years)
        # 退出
        elif choice == "q":
            print("欢迎下次光临！再见！")
            break
        else:
            print("你输入的指令有误，请重新输入\n")
if __name__ == '__main__':
    main()

#64.实例一：删除字符串首尾的空格：可以使用 strip()方法，返回新的字符串，不改变原字符串。
original_string = "   这是一个带有空格的字符串   "
stripped_string = original_string.strip()
print(stripped_string)
#实例二：如果字符串中有 \n 等字符，并且您只想删除空格，则需要在strip()方法上显式指定它
my_string="   \nPython   "
print(my_string.strip(" ")) #指定去除空白字符，不包含换行符。
#实例三：使用正则表达式来删除字符串首尾的空格：
import re
my_string="   Hello Python   "
output=re.sub(r'^\s+|\s+$','',my_string) #意思是用""替代首位的空白字符。
print(output)
#实例四：lstrip()删除字符串开头的空格。rstrip()删除字符串结尾的空格。
original_string ="    这是一个带有空格的字符串     "
left_stripped_string = original_string.lstrip()  # 删除开头的空格
right_stripped_string = original_string.rstrip()  # 删除结尾的空格
print(left_stripped_string)
print(right_stripped_string)

#65.按字母顺序对列表排序
#实例一：sort()方法，即直接修改原始列表，该方法会改变原列表的顺序。
my_list = ["apple", "banana", "cherry", "date"]
my_list.sort()  # 按字母顺序排序
print(my_list)
#实例二：sorted()函数，创建一个新的已排序列表，不修改原始列表，函数返回一个新的已排序列表，原列表保持不变。
my_list = ["apple", "banana", "cherry", "date"]
sorted_list = sorted(my_list)  # 创建一个新的已排序列表
print(sorted_list)
#无论你选择哪种方法，都可以按字母顺序对列表进行排序。
# 如果你希望按字母顺序的反向顺序排序（降序），可以在 sort() 方法或 sorted() 函数中传递 reverse=True 参数。

#66.创建一个简单的任务清单（to-do list）
tasks = [] #创建一个空的任务列表
def add_task(task): # 定义函数来添加任务
    tasks.append(task)
    print(f"任务 '{task}' 已添加.")
def show_tasks(): # 定义函数来显示任务列表
    if not tasks:
        print("任务清单是空的.")
    else:
        print("任务清单:")
        for index, task in enumerate(tasks, start=1): #遍历任务清单，返回索引及其对应任务，指定索引从1开始。
            print(f"{index}.{task}")
while True: # 主程序循环
    print("\n选择一个选项:")
    print("1. 添加任务")
    print("2. 显示任务清单")
    print("3. 退出")
    choice = input("输入选项编号: ")
    if choice == "1":
        new_task = input("输入新任务: ")
        add_task(new_task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        print("退出程序.")
        break
    else:
        print("无效的选项，请重新输入.")

#66.判断一个数是否为质数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): #根据质数的性质，如果n质数，则它必有一个因子<n的平方根。遍历到n**0.5节省计算资源
        if n % i == 0:
            return False
    return True
# 测试函数
number = 29
if is_prime(number):
    print(f"{number} 是质数")
else:
    print(f"{number} 不是质数")

#67.计算字符串中每个字母的出现次数（用字典）
def count_letters(s):
    letter_count={} #建立一个空字典
    for char in s: #遍历字符串每个字符
        if char in letter_count:
            letter_count[char] += 1 #检测字符是否在字典中，如存在，则value+1
        else:
            letter_count[char] = 1 #如果不在的话，则将字符加入字典中，value设为1
    return letter_count
# 示例字符串
text = "hello world"
result = count_letters(text)
print(result)

#68.检查列表是否包含重复项：过将列表转换为集合来检查列表中是否包含重复项
def has_duplicates(lst):
    return len(lst) != len(set(lst))
# 示例列表
example_list = [1, 2, 3, 4, 5, 2]
# 检查是否有重复项
if has_duplicates(example_list):
    print("列表包含重复项")
else:
    print("列表不包含重复项")

#69.求两个字符串的最长公共子串
def longest_common_substring(s1, s2):
    m = len(s1)
    n = len(s2)
    # 创建一个二维数组来存储最长公共子串的长度
    dp = [[0] * (n + 1) for _ in range(m + 1)] #每个元素初始化为0，用于存储s1前i个字符和s2前j个字符的LCS长度
    max_length = 0  # 记录最长公共子串的长度
    end_pos = 0     # 记录最长公共子串的结束位置
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]: #相同字符
                dp[i][j] = dp[i-1][j- 1]+1 #长度加1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_pos = i
            else:
                dp[i][j] = 0
    # 返回最长公共子串
    return s1[end_pos - max_length:end_pos]
# 测试
s1 = "abcdef"
s2 = "zbcdf"
result = longest_common_substring(s1, s2)
print("最长公共子串是:", result)

#70.找到两个字符串的差异：difflib模块提供了一个Differ类，它可以逐行比较两个字符串，并生成一个差异报告。
import difflib
def find_string_differences(str1, str2):
    differ = difflib.Differ() #创建一个 Differ 对象，用于比较两个字符串。
    diff = differ.compare(str1.splitlines(), str2.splitlines()) #使用 Differ 对象的 compare 方法来比较两个字符串的每一行。splitlines() 方法将字符串按行分割成列表。
    return 'n'.join(diff) #将比较结果拼接成一个字符串并返回。
str1 = """"""Hello world!
This is a test.
Python is fun."""
str2 = """Hello world!
This is a test.
Python is awesome.""""""

differences = find_string_differences(str1, str2)
print(differences)

#71.创建一个类并实例化它
class Dog: #定义了一个名为 Dog 的类
    def __init__(self, name, age): #是类的构造函数，用于初始化对象的属性。self 表示类的实例本身，name 和 age 是传递给构造函数的参数。
        self.name = name #将传入的参数赋值给实例的属性。
        self.age = age
    def bark(self): #定义了一个名为bark的方法，它返回一个字符串，表示狗叫的声音。
        return f"{self.name} says woof!"
# 实例化类：创建了一个 Dog 类的实例，并传递了 "Buddy" 和 3 作为参数。
my_dog = Dog("Buddy", 3)
# 访问属性和调用方法
print(my_dog.name)
print(my_dog.age)
print(my_dog.bark())

#72.实现一个基于类的矩阵类：这个类将帮助我们理解如何在 Python 中使用类来封装数据和操作。
class Matrix: #定义一个矩阵类
    def __init__(self, data): #构造函数:接受一个二维列表作为参数，并计算矩阵的行数和列数。
        self.data = data
        self.rows = len(data) #行是data的长度
        self.cols = len(data[0]) if self.rows > 0 else 0 #data[0]表示二维矩阵第一行列表，它的长度即为列数。
    def __add__(self, other): #矩阵加法
        if self.rows != other.rows or self.cols != other.cols: #检查两个矩阵的维度是否相同
            raise ValueError("Matrices must have the same dimensions for addition.")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)] #使用列表推导式实现逐元素相加
        return Matrix(result)
    def __mul__(self, other): #矩阵乘法
        if self.cols != other.rows: #检查第一个矩阵的列数是否等于第二个矩阵的行数
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(result)
    def transpose(self): #矩阵转置方法
        result = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)] #交换行列索引实现转置
        return Matrix(result)
    def __str__(self): #字符串表示方法
        return '\n'.join([' '.join(map(str, row)) for row in self.data]) #将矩阵每行转换为空格分隔的字符串，用换行符连接各行
# 示例使用
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
print("Matrix 1:")
print(m1)
print("Matrix 2:")
print(m2)
print("Matrix 1 + Matrix 2:")
print(m1 + m2)
print("Matrix 1 * Matrix 2:")
print(m1 * m2)
print("Transpose of Matrix 1:")
print(m1.transpose())

#73.使用 `filter` 和 `map` 函数处理数据
#假设我们有一个包含数字的列表，我们想要过滤出所有的偶数，并将这些偶数乘以2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 定义一个包含数字的列表
even_numbers = filter(lambda x: x % 2 == 0, numbers) # 使用 filter 函数过滤出偶数
doubled_even_numbers = map(lambda x: x*2, even_numbers) # 使用 map 函数将偶数乘以 2
# 将结果转换为列表并打印
result = list(doubled_even_numbers)
print(result)"""

#74.使用 Python 读取并写入 CSV 文件
import csv
# 读取 CSV 文件
with open('input.csv', mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    data = [row for row in reader]
# 写入 CSV 文件
with open('output.csv', mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)

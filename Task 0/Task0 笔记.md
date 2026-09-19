# Task 0 代码积累（自用）

## 输入
input 输入默认为字符串形式，要转化为整数型应为 int(input())
加 split() 表示以空格为间隔
```
a , b = map(int,input().split)
```
## 输出
print 默认以换行 (/n) 为 end
设置 end ：
``` python
 print(a,sep=" ")
 ```
## List

list 下标从零开始
### 输入
```
nums = list(map(int,input().split()))
nums.append()    ##从末尾加入
nums.insert(1," 1") ##指定位置插入，不替换
nums.extend([1,2])  ##从末尾加入多个元素
nums[1] = "2" 
```

### 修改
```
nums.remove("1") ##删除第一个"1"
last = nums.pop() ##删除并返回最后一个元素
del nums[1] ## 删除指定下标的元素
nums.clear
```

### 排序与反转
```
nums.sort ##升序排列
nums.sort(reverse = True) ##降序排列
nums.reverse ##反转
```

### 切片操作
```
print(nums[strat:stop:step])
```

### 查询与统计
```
nums.index("1") ## 返回出现该元素的下标
nums.count("1") ## 返回出现该元素的次数
"1" in nums ## 判断是否出现该元素
```

## for 
记得加冒号




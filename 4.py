#range
y = 0
for i in range(5,10,2):
    y= i*i+y
print(y)
#tuple
ti = 20, "fuck"
print(ti)
print(type(ti)) #辨識類型方法
#list
a = [1, 2, 3]
a[0] = [6, 7, 8]
print (a[0], a[1])
#strung (字串)
s1 = "i"
s1 += " hate python"
print (s1)
s2 = s1.split()
print(s2)
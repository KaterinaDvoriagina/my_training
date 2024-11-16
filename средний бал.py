grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}

a = grades[:1] = [(5+3+3+5+4)/5]
b = grades[:2] = [(2+2+2+3)/4]
c = grades[:3] = [(4+5+5+2)/4]
d = grades[:4] = [(4+4+3)/3]
e = grades[:5] = [(5+5+5+4+5)/5]
a = sum(a)
b = sum(b)
c = sum(c)
d = sum(d)
e = sum(e)
my_list = list(students)
sorted_list =sorted(my_list)
ball = {sorted_list[0]:a,sorted_list[1]:b,sorted_list[2]:c,sorted_list[3]:d,sorted_list[4]:e}
print(ball)
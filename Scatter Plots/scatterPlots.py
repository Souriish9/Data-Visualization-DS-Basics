import matplotlib.pyplot as plt

f=open('salesdata2.csv','r')
salefile=f.readlines()

s_list=[]
c_list=[]

for records in salefile:
    sale,cost=records.split(',')
    s_list.append(int(sale))
    c_list.append(int(cost))

plt.title('Sales vs Cost')
plt.xlabel('Sale')
plt.ylabel('Cost')

plt.scatter(s_list,c_list)
plt.show()
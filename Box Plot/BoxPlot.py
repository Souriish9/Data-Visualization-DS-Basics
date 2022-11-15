import matplotlib.pyplot as plt

dataset=open('salesdata.csv','r')
salefile=dataset.readlines()

sale_list=[]

for records in salefile:
    sale_list.append(int(records))

plt.title('Box of sales')
plt.boxplot(sale_list,showfliers=None)
plt.show()
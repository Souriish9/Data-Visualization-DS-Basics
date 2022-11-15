import matplotlib.pyplot as plt


# --------------------------piechart----------------------------------
f1=open('agedata2.csv','r')
agefile=f1.readlines()

city_list=[]

for records in agefile:
    #use the split function
    age,city=records.split(',')
    city_list.append(city)

from collections import Counter
city_count=Counter(city_list)

city_names=list(city_count.keys())
city_values=list(city_count.values())

plt.subplot(2,2,1)
plt.pie(city_values,labels=city_names,autopct='%.2f%%')
#plt.show()


# -----------------------Histogram--------------------------

#open the file in read mode
f2=open('agedata.csv','r')

agefile=f2.readlines()

# Integer list
age_list=[]

for records in agefile:
    age_list.append(int(records))

bins=[]
for i in range(0,101,10):
    bins.append(i)

plt.subplot(2,2,2)
plt.title('Age Histogram')
plt.xlabel('Group')
plt.ylabel('Age')

plt.hist(age_list,bins,histtype='bar',rwidth=0.9)
#plt.show()

#-----------------------------Box Plot--------------------------------------

dataset=open('salesdata.csv','r')
salefile=dataset.readlines()

sale_list=[]

for records in salefile:
    sale_list.append(int(records))

plt.subplot(2,2,3)
plt.title('Box of sales')
plt.boxplot(sale_list,showfliers=None)
#plt.show()

#------------------------------ Scatter Plots----------------------------------

f3=open('salesdata2.csv','r')
salefile=f3.readlines()

s_list=[]
c_list=[]

for records in salefile:
    sale,cost=records.split(',')
    s_list.append(int(sale))
    c_list.append(int(cost))

plt.subplot(2,2,4)
plt.title('Sales vs Cost')
plt.xlabel('Sale')
plt.ylabel('Cost')

plt.scatter(s_list,c_list)

# adding a tight layout, saving the pic & displaying the fig
plt.tight_layout()
plt.savefig('subplot.png')
plt.show()

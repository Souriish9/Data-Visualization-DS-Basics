import matplotlib.pyplot as plt

#open the file in read mode
f=open('agedata.csv','r')

agefile=f.readlines()

# Integer list
age_list=[]

for records in agefile:
    age_list.append(int(records))

bins=[]
for i in range(0,101,10):
    bins.append(i)

plt.title('Age Histogram')
plt.xlabel('Group')
plt.ylabel('Age')

plt.hist(age_list,bins,histtype='bar',rwidth=0.9)
plt.show()

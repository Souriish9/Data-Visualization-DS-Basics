import matplotlib.pyplot as plt

#Plot a bar chart
x_cities=['Kolkata','Lucknow','Coimbatore','Gawhati','Pune']
y_temp=[75,65,105,98,90]

plt.title('Temperature Variations')
plt.xlabel('Cities')
plt.ylabel('Temperature')

plt.bar(x_cities,y_temp)

plt.show()
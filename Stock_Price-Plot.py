#define the libraries
import matplotlib.pyplot as plt

#define the values
x_days=[1,2,3,4,5]
y_price1=[9,9.5,8,10,9.6]
y_price2=[11,12,10.5,11.5,12.9]

# add titles & labels
plt.title('Stock Price')
plt.xlabel('Week Days')
plt.ylabel('Price in USD')

#plot
plt.plot(x_days,y_price1, label='Stock 1')
plt.plot(x_days,y_price2,label='Stock 2')

# add legends
plt.legend(loc=2,fontsize=12)

#show the plot
plt.show()
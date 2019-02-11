import  matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

x3_values =list(range(1,5001))
y3_values = [x**3 for x in x3_values]

plt.scatter(x_values,y_values,s=4,edgecolor='none',c=y_values,cmap=plt.cm.Blues)

# 设置图像标题，并给坐标轴加上标签
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#
plt.tick_params(axis='both',labelsize=14,which='major')

plt.axis([0,1100,0,1100000])

plt.savefig('square_plot.png',bbox_inches='tight')
plt.show()

plt.scatter(x3_values,y3_values,s=4,edgecolor='none',c=y3_values,cmap=plt.cm.pink)

plt.axis([0,5000,0,5000**3])
plt.show()


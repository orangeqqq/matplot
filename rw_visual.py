import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    #设置图像分变率与大小
    plt.figure(dpi=128,figsize=(10,6))

    point_numbers = list(range(rw.num_points))
    #plt.scatter(rw.x_values,rw.y_values,s=1,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none')
    
    plt.plot(rw.x_values,rw.y_values)

    #突出起点和终点

    plt.scatter(0,0,c='green',edgecolor='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',s=100)

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)



    
    
    


    plt.show()

    keep_running = input("make another walk?(y/n)")
    if keep_running == 'n':
        break

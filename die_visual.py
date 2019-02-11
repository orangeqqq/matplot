from die import Die
import pygal

die_1 = Die()
die_2 = Die(10)

#掷几次骰子，结果存入列表
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析结果
frequencies=[]
max_result = die_1.num_sides +die_2.num_sides
for value in range(2,1+max_result):
    frequency = results.count(value)
    frequencies.append(frequency)

#结果可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times"

hist.x_title = "results"
hist.y_title = "Frequency of Results"
hist.x_labels = []
for num in range(2,max_result+1) :
    string = str(num)
    hist.x_labels.append(string)


hist.add('D6+D10',frequencies)
hist.render_to_file('dice_visual.svg')




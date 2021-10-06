import matplotlib.pyplot as plt
days = [1,2,3,4,5]
Enfield =[50,40,70,80,20]
Honda = [80,20,20,50,60]
Yahama =[70,20,60,40,60]
KTM = [80,20,20,50,60]
slices = [8,5,5,6]
activities = ['Enfield','Honda','Yahama','KTM']
cols = ['c','g','y','b']
plt.pie(slices, labels=activities, colors=cols, startangle=90, shadow= True, explode=(0,0.1,0,0), autopct='%1.1f%%')
plt.title('Bike details in Pie Plot')
plt.show()
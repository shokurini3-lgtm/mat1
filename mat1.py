import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
scores = [30,90,21,10,64]



plt.plot(days,scores, color='green', marker='o',
         linestyle='dashed', linewidth=2)
plt.title('my quiz score tracker')
plt.xlabel('Days of the week')
plt.ylabel('Scores')
plt.grid(True)
plt.ylim(0,100)
plt.show()


plt.bar(days,scores, color='blue')
plt.title('my quiz score bar chart')
plt.xlabel('Days of the week')
plt.ylabel('Score')
plt.ylim(0,100)
plt.show()
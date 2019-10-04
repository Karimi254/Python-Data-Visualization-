#! /usr/bin/python3.6

from matplotlib import pyplot as plt  
plt.style.use('classic')

minutes = [1,2,3,4,5,6,7,8,9]

Developer_A = [8, 6, 5, 5, 4, 2, 1, 1, 0]
Developer_B = [0, 1, 2, 2, 2, 4, 4, 4, 4]
Developer_C = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['Developer_A', 'Developer_B', 'Developer_C']

plt.stackplot(minutes, Developer_A, Developer_B, Developer_C, labels=labels)

plt.title('8-hr Developer Performance Stack Plot')

plt.legend(loc=(0.07, 0.05))
plt.tight_layout()

plt.savefig('developer_performance3.png')
plt.show()
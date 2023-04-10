import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

data = np.loadtxt("data.csv", dtype=int)
ages = data[:, 0]
men = data[:, 1]
women = data[:, 2]


fig, ax = plt.subplots(figsize=(15, 7))
#plt.tight_layout()

ax.barh(ages, -men, color='navy')
ax.barh(ages, women, color='violet')

ax.barh(ages, men, color='blue', align='center', label='men')
ax.barh(ages, -women, color='pink', align='center', label='women')


ax = plt.gca()
ax.spines['left'].set_position('zero')

ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
plt.tick_params(axis='y', which='major', labelsize=4)
plt.ylim([0, 100])

ax.set_xlabel('Population')

ax.set_title('Age-sex pyramid')
ax.legend()
plt.show()



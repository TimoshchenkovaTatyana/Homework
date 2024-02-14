'''
import matplotlib.pyplot as plt
fig = plt.figure()

x=['математика','русский язык','английский язык', 'физика', 'информатика', 'французский язык']
y=[9.8, 7, 6.5, 10, 10, 3]

plt.plot(x, y)

plt.show()

import matplotlib.pyplot as plt
import numpy as np
k=float(input())
b=float(input())
x = np.linspace(-100, 100, 1000)
y=k*x+b
fig = plt.figure()
plt.plot(x,y)
plt.show()


--------------------------------------------


import matplotlib.pyplot as plt
import numpy as np

k = float(input())
b = float(input())

x = np.linspace(-100, 100, 1000)
y = k*x+b
fig = plt.figure

fig, ax = plt.subplots()
ax.plot(x, y)
plt.grid(True)

plt.show()

----------------------------------------


import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y = 3+x**2-14*x-9
y1 = np.arange(0, 10, 0)


plt.plot(x, y, label = 'plot')
plt.scatter(x, y1, color = 'red', label =  'Scatter')
plt.text(5,25,"Hello World", fontsize = 23, bbox = dict(alpha = 0.5, color = "orange"))


plt.legend()
plt.grid()
plt.show()

----------------------



import matplotlib.pyplot as plt
import numpy as np


disciplines = (
    'Русский',
    'Профиль',
    'Общество',
    'Биология',
    'Физика',
    'История',
    'Информатика',
    'Химия',
    'Литература',
    'География',
    'Английский'
)
students = {
    "2022": np.array([78.3, 68.3, 60.8, 59.5, 54.6, 59.8, 56.8, 54.1, 57.9, 54.3, 50.2]),
    "2023": np.array([66.31, 66.43, 63.97, 58.39, 53.6, 56.4, 55.62, 54.95, 56.37, 56.23, 50.38]),
}

width = 0.5
bottom = np.zeros(11)
fig, ax = plt.subplots()

for year, st in students.items():
    p = ax.bar(disciplines, st, width, label = year, bottom = bottom)
    bottom+=st
plt.show()

-----------------------------

a = int(input())
b = int(input())

if a>b:
    c=a
    a=b
    b=c
from random import randint
A = [0]*10
for i in range(0,5):
    A[i] = randint(a,b)
for i in range(5, 10):
    A[i]=A[i-5]*A[i-5]
print(*A)

----------------------------------

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

x_1 = np.arange(20)
y_1 = x_1 ** 3

x_2 = np.arange(20)
y_2 = 3*x_2 - 8

plt.fill(x_1, y_1, 'g')

plt.text(10,0.5, 'текст', horizantalalignment = 'center'
bbox = dict(farecolor = 'p', alpha = 0.2))

plt.grid(True)
plt.show()
------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y = 3+x**2-14*x-9
y1 = np.arange(0, 10, 0)


plt.plot(x, y, label = 'plot')
plt.scatter(x, y1, color = 'red', label =  'Scatter')
plt.text(5,25,"Hello World", fontsize = 23, 
bbox = dict(alpha = 0.5, color = "orange"))


plt.legend()
plt.grid()
plt.show()

----------------------
import matplotlib.pyplot as plt
import numpy as np


disciplines = (
    'Русский',
    'Профиль',
    'Общество',
    'Биология',
    'Физика',
    'История',
    'Информатика',
    'Химия',
    'Литература',
    'География',
    'Английский'
)
students = {
    "2022": np.array([78.3, 68.3, 60.8, 59.5, 54.6, 59.8, 56.8, 54.1, 57.9, 54.3, 50.2]),
    "2023": np.array([66.31, 66.43, 63.97, 58.39, 53.6, 56.4, 55.62, 54.95, 56.37, 56.23, 50.38]),
}

width = 0.5
bottom = np.zeros(11)
fig, ax = plt.subplots()

for year, st in students.items():
    p = ax.bar(disciplines, st, width, label = year, bottom = bottom)
    bottom+=st

plt.text('физика', 60, 'Так и живем', fontsize = 23, horizontalalignment = 'center', 
        bbox = dict(facecolor = "blue", alpha = 0.2))
plt.show()
'''



import matplotlib.pyplot as plt
import numpy as np

y = np.random.random(100)
fig = plt.figure()
histo = plt.hist(y)

plt.ylabel('Light weight', {'fontname': 'Consolas'})
plt.text(0.1, 10, 'text', {'fontname': 'Consolas'})

plt.grid(True)
plt.show()
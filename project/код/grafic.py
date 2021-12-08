import matplotlib.pyplot as plt


balltd = [16074.90,23695.10,7435.00]
balltd1 = [12039.50,18042.10,1782.00]
balrad = [406.90,889.50,1017.50]
balrad1 = [326.20,729.40,817.50]
balun = [2277.00,4400.00,15266.50]
balun1 = [1512.00,3260.00,14348.50]
period = ["базовий","попередній","поточний"]

plt.plot(period,balltd,balltd1,label = "Дружба ЛТД")
plt.plot(period, balrad,balrad1, label = "Радунь")
plt.plot(period, balun, balun1, label = "Універмаг")
plt.xlabel("Період")
plt.ylabel("Прибуток")
plt.legend()
plt.grid(True)

def showplot():
 plt.show()
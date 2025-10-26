import matplotlib.pyplot as plt
import numpy as np

# תרגילים
# תרגיל 1
x = ["תשרי","חשון","כסליו","טבת","שבט","אדר","ניסן","אייר","סיון","תמוז","אב","אלול"]
y = [23.5, 22, 15.5, 11, 15, 20, 23, 25, 25, 28.5, 28.5, 27]
plt.title("שינויי הטמפרטורות לאורך השנה")
plt.xlabel("חודש")
plt.ylabel("טמפרטורה ממוצעת (°C)")
plt.plot(x, y)
plt.show()

# תרגיל 2
categories = ["בגדים","אוכל","תכשיטים","אביזרי גינה"]
count = [35, 50, 25, 30]
plt.bar(categories, count)
plt.title('כמות מחירות לכל קטגוריה')
plt.xlabel('Categories')
plt.ylabel('Count')
plt.show()

# תרגיל 3
hours = [1, 5, 2, 7, 3, 4, 6, 8, 10, 9]
grade = [78, 89, 90, 100, 85, 77, 63, 95, 96, 45]
colors = "red"
# sizes = 1000 * np.random.rand(10)
plt.scatter(hours, grade, c=colors, alpha=0.5, cmap='viridis')
plt.colorbar()  # הצגת סרגל הצבעים
plt.title('הקשר בין זמן לימוד לציון במבחן')
plt.xlabel('שעות לימוד')
plt.ylabel('ציון במבחן')
plt.show()

# תרגיל 4
ages = [15, 35, 45, 10, 22, 40, 33, 56, 47, 27, 53, 49, 12, 31]
plt.hist(ages, bins=[10, 20, 30, 40, 50, 60], color="pink",  edgecolor='black')
plt.title('התפלגות גילאים בקבוצת נבדקים')
plt.xlabel('Ages')
plt.ylabel('Number of People')
plt.show()

# תרגיל 5
years = range(2010, 2021)
consumption_oil = [100, 105, 110, 120, 125, 130, 135, 140, 145, 150, 155]
consumption_gas = [80, 82, 85, 88, 90, 95, 100, 105, 110, 115, 120]
consumption_renewable = [20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90]
plt.plot(years, consumption_oil, '-b', label='Consumption oil')
plt.plot(years, consumption_renewable, ':r', label='Consumption renewable')
plt.title('השוואה בין צריכת אנרגיה למקורות לפי שנים')
plt.legend()
plt.show()
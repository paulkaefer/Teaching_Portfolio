import matplotlib.pyplot as plt

# data from https://www.accuweather.com/en/us/minneapolis/55415/october-weather/348794
MN_October_temps = [72, 75, 76, 78, 73, 61, 49, 64, 69, 71, 80, 63, 45, 42]

plt.plot(MN_October_temps)
plt.title('October high temperatures: MN')
plt.xlabel('Day')
plt.ylabel('Temperature (°F)')
plt.show()




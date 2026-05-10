
celsius_temperatures = [0, 10, 25, 32, 100]
fahrenheit_temperatures = [] 


for celsius in celsius_temperatures:
  fahrenheit = (celsius * 9/5) +32

  fahrenheit_temperatures.append(fahrenheit)


print("Celsius Temperatures:", celsius_temperatures)
print("Fahrenheit Temperatures:", fahrenheit_temperatures)
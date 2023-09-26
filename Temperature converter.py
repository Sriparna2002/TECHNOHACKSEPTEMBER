unit = input("Is this temparature in Fahrenheit or Celsius (C/F):  ")
temp = float(input("Enter the temparature : "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32 , 1)
    print(f"The temparature in Fahrenheit is: {temp}°F")
elif unit =="F":
    temp = round((temp-32) * 5 / 9 , 1)
    print(f"The temparature in Celsius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")
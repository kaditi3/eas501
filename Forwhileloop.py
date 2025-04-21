daily_usage = [30, 28, 32, 31, 29,35, 33]
total_usage=0

for i in range(0,7):
    total_usage+= daily_usage[i]
print(f"the total usage is:{total_usage} kWh")

daily_usage = [30, 28, 32, 31, 29,35, 33]
i=0
total_usage=0

while i<len(daily_usage):
      total_usage += daily_usage[i]
      i+=1
print(f"the total usage is:{total_usage} kWh")

Temp = [15, 18, 22, 19, 25, 28, 21]
Day =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i in Temp:
  if Temp[i]>24:
    print(f"First day with exceed 24 is:" Day[i])
    break
  print(f"Temp is below 24")
    

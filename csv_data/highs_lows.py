import csv 

from matplotlib import pyplot as plt
from datetime import datetime as dt

filename= "../pcc_3e-main/chapter_16/the_csv_file_format/partial_programs/weather_data/sitka_weather_2021_full.csv"

with open(filename) as fn: 
    reader = csv.reader(fn) #creates a csv reader object
    header_row = next(reader) #converts the reader obj's output into a list
    

    dates, highs, lows = [], [], []
    """    for index, column_header in enumerate(header_row):
        print(index, column_header)"""

    for row in reader:
        try: 
            current_date = dt.strptime(row[2], "%Y-%m-%d")

            high = int(row[7])

            low = int(row[8])
        except ValueError:
            print(current_date, "Missing data point")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    
# #plot data
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

#format plot
plt.title("Daily high temperatures - 2021", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
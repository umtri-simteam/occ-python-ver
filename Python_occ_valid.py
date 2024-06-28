
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

# Take the file path from command-line arguments
if len(sys.argv) < 2:
    print("Usage: python script.py <file_name>")
    sys.exit(1)

file_path = sys.argv[1]

# Load the data from the file
data = pd.read_csv(file_path, header=None, names=['Values'])
# file_path = file_path.replace(".txt", "")

# Multiply data values by 1000
data['Values'] = data['Values'][0:1069] * 1000

# Calculate statistics
statistics = {
    'Min': data['Values'].min(),
    'Max': data['Values'].max(),
    'Q1': data['Values'].quantile(0.25),
    'Median': data['Values'].median(),
    'Q3': data['Values'].quantile(0.75),
    'Mean': data['Values'].mean(),
    'STD': data['Values'].std()
}

# Create a DataFrame for the statistics
stats_df = pd.DataFrame(statistics, index=[0])

# Print the statistics table
print(stats_df)

# Calculate the y-axis range based on the average
mean_value = statistics['Mean']
std_dev = statistics['STD']
y_min = mean_value - 3 * std_dev
y_max = mean_value + 3 * std_dev

# Plot the data with adjusted y-axis range
plt.figure(figsize=(10, 6))
plt.bar(range(len(data)), data['Values'])
plt.xlabel('Index')
plt.ylabel('Values (mm)')
# plt.title('Bar Plot of Data Values')
plt.ylim(y_min, y_max)
plt.axhline(mean_value, color='red', linestyle='--', label='Mean')

# Add Q1 and Q3 lines
q1_value = statistics['Q1']
q3_value = statistics['Q3']
plt.axhline(q1_value, color='blue', linestyle='--', label='Q1')
plt.axhline(q3_value, color='green', linestyle='--', label='Q3')

plt.legend()
# Save the plot as an image
# Plot_name = file_path + "_plot.png"
plt.savefig("plot.png")
plt.show()


# Save the statistics table to a CSV file
# CSV_name = file_path + "_statistics.csv"
stats_df.to_csv("statistics.csv", index=False)

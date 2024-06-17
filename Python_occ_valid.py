import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the file
file_path = 'script_out.txt'
data = pd.read_csv(file_path, header=None, names=['Values'])

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
plt.ylabel('Values')
plt.title('Bar Plot of Data Values')
plt.ylim(y_min, y_max)
plt.axhline(mean_value, color='red', linestyle='--', label='Mean')
plt.legend()
plt.show()

# Save the statistics table to a CSV file
stats_df.to_csv('statistics.csv', index=False)

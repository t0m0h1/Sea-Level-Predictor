import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

    # First Line of Best Fit (Using All Data)
    res = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    x_pred_1 = pd.Series(range(1880, 2051))
    y_pred_1 = res.intercept + res.slope * x_pred_1
    plt.plot(x_pred_1, y_pred_1, 'r', label="Best Fit (1880-2050)")

    # Second Line of Best Fit (Using Only Data From 2000 Onward)
    data_recent = data[data['Year'] >= 2000]  # Ensure only data from 2000 onward is used
    res_recent = linregress(data_recent['Year'], data_recent['CSIRO Adjusted Sea Level'])

    x_pred_2 = pd.Series(range(2000, 2051))  # Predict from 2000 to 2050
    y_pred_2 = res_recent.intercept + res_recent.slope * x_pred_2
    plt.plot(x_pred_2, y_pred_2, 'g', label="Best Fit (2000-2050)")

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

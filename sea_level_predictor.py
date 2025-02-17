import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Create lines of best fit
    x = data['Year']
    y = data['CSIRO Adjusted Sea Level']
    res = linregress(x, y)

    x_pred = pd.Series(range(1880, 2051))
    y_pred = res.intercept + res.slope * x_pred
    plt.plot(x_pred, y_pred, 'r')

    x_second = pd.Series(range(2000, 2051))
    y_second = res.intercept + res.slope * x_second
    plt.plot(x_second, y_second, 'g')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
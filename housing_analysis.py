import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_data(x, y, ylim):
    data = pd.concat([housing_data[y], housing_data[x]], axis=1)
    with sns.plotting_context("notebook", font_scale=1.5):
        sns.set_style("whitegrid")
        sns.pairplot(data, height=3)
        plt.show()

# Load data of housing
housing_data = pd.read_csv('housing_data.csv')

# check the columns my dataframe have
housing_data.columns

# look for description of sales price
housing_data['SalePrice'].describe()

# Visualize with distribution plot on the sales prices
sns.displot(housing_data['SalePrice'])
plt.show()
plt.clf()

# concatenate the sales price with the first flor SF and visualize the relationship
plot_data('1stFlrSF', 'SalePrice', ylim=(0,800000))

# concantenate the sales price and garage are data and visualize the relationship between the two
plot_data('GarageArea', 'SalePrice', ylim=(0,800000))

# concantenate the sales price and year built are data and visualize the relationship between the two
plot_data('YearBuilt', 'SalePrice', ylim=(0,800000))

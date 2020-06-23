import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

plt.style.use(style='ggplot')

train = pd.read_csv(Path('./train.csv'))
plt.scatter(train.GarageArea, train.SalePrice, alpha=.5, color='black')
plt.show()

filter_data = train[(train.GarageArea > 150) & (train.GarageArea < 900) & (train.SalePrice < 500000)]
plt.scatter(filter_data.GarageArea, filter_data.SalePrice, alpha=.5, color='r')
plt.show()
print("GarageArea", train.GarageArea)
print("SalePrice", train.SalePrice)

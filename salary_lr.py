import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
customers=pd.read_csv("EcommerceCustomers.csv")
print(customers.head())
print(customers.describe())
sns.set_palette('GnBu_r')
sns.jointplot(x='Time on Website',y='Yearly Amount Spent',data=customers)
plt.show()
sns.jointplot(x='Time on App',y='Yearly Amount Spent',data=customers)
plt.show()
sns.jointplot(x='Time on App',y='Length of Membership',data=customers,kind='hex')
plt.show()
sns.jointplot(x='Time on Website',y='Length of Membership',data=customers,kind='hex')
plt.show()
sns.pairplot(customers)
plt.show()
sns.pairplot(customers)
plt.show()


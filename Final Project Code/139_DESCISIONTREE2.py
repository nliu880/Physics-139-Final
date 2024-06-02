import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
random_state = 3

Boosting_data = pd.read_csv("Data/BoostingData.csv")

X = Boosting_data.values[:,3:]
y = Boosting_data.values[:,2]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=random_state)
X_train = np.asarray(X_train.astype("float32"))
X_test = np.asarray(X_test.astype("float32"))



from xgboost import XGBRegressor



bdt = XGBRegressor(n_estimators=100,max_depth=3,learning_rate=0.1,colsample_bytree=0.8, subsample=0.8)
print(bdt)
bdt.fit(X_train, y_train)
preds_bdt = bdt.predict(X_test)


import xgboost as xgb
#xgb.plot_importance(bdt)
plt.scatter(preds_bdt, y_test)
plt.plot(np.arange(200, 400), np.arange(200,400), color= "r")
plt.xlabel('Predicted energy values') 
plt.ylabel('Actual energy values')
plt.legend()
plt.title("Predicted vs Actual energy values")
plt.savefig("Plots/predicted_actual_energy")
plt.show()

#second descision tree

X2= X_test
y2= preds_bdt - y_test

X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.1, random_state=random_state)
X2_train = np.asarray(X2_train.astype("float32"))
X2_test = np.asarray(X2_test.astype("float32"))



bdt2 = XGBRegressor(n_estimators=100,max_depth=3,learning_rate=0.1,colsample_bytree=0.8, subsample=0.8)
print(bdt2)
bdt2.fit(X2_train, y2_train)
preds_bdt2 = bdt2.predict(X2_test)


plt.scatter(preds_bdt2, y2_test)
#plt.plot(np.arange(200, 400), np.arange(200,400), color= "r")
plt.xlabel('Predicted energy values') 
plt.ylabel('Actual energy values')
plt.legend()
plt.title("Predicted vs Actual energy values")
plt.savefig("Plots/second_descision_tree_actual_energy")
plt.show()


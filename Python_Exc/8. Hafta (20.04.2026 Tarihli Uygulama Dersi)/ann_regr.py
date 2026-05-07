
import numpy as np
import pandas as pd
#pip install scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error
from sklearn.metrics import median_absolute_error, r2_score
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

# Veri setini oku
veriseti = pd.read_csv('Ann.csv')

# Girdi ve hedef
X = veriseti.iloc[:, :-1].values #üm satırları al, son sütun hariç tüm sütunları al
y = veriseti.iloc[:, -1].values #son sütun hedef sütununu al

# Eğitim ve test veri kümelerine ayırma
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Ölçeklendirme
scaler_X = MinMaxScaler()
scaler_y = MinMaxScaler()

X_train = scaler_X.fit_transform(X_train)
X_test = scaler_X.transform(X_test)

y_train = y_train.reshape(-1, 1) #-1 satır sayısını otomatik belirle, 1 sütunlu liste yap
y_test = y_test.reshape(-1, 1)

y_train_scaled = scaler_y.fit_transform(y_train)
y_test_scaled = scaler_y.transform(y_test)

# ANN regresyon modeli
model = Sequential()
model.add(Dense(16, kernel_initializer='he_uniform', activation='relu', input_dim=X_train.shape[1]))
model.add(Dense(16, kernel_initializer='he_uniform', activation='relu'))
model.add(Dense(1, kernel_initializer='he_uniform', activation='linear'))

# Derleme

model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')

# Eğitim
model.fit(X_train, y_train_scaled, batch_size=8, epochs=100, verbose=1)

# Tahmin
y_pred_scaled = model.predict(X_test)

# Orijinal ölçeğe geri çevir
y_pred = scaler_y.inverse_transform(y_pred_scaled)
y_test_original = scaler_y.inverse_transform(y_test_scaled)

# Performans değerlendirme
print("Explained Variance:", explained_variance_score(y_test_original, y_pred))
print("R_2:", r2_score(y_test_original, y_pred))
print("MAE:", mean_absolute_error(y_test_original, y_pred))
print("MSE:", mean_squared_error(y_test_original, y_pred))
print("MedAE:", median_absolute_error(y_test_original, y_pred))

#hidden units: 8, 16, 32
#hidden layer count: 1, 2, 3
#batch_size: 8, 16, 32
#epochs: 50, 100, 150
#optimizer: adam, rmsprop, sgd
#learning_rate: 0.01, 0.001, 0.0001
#activation: relu, tanh, sigmoid, linear
#initializer: he_uniform, glorot_uniform, uniform
#test_size: 0.2, 0.3, 0.4

#from keras.optimizers import SGD
#model.compile(optimizer=SGD(learning_rate=0.001), loss='mean_squared_error')

#from keras.optimizers import RMSprop
#model.compile(optimizer=RMSprop(learning_rate=0.001), loss='mean_squared_error')
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

from keras.models import Sequential
from keras.layers import Dense

# Veri setini oku
veriseti = pd.read_csv("immuno.csv")

# Girdi ve hedef
X = veriseti.iloc[:, :-1].values
y = veriseti.iloc[:, -1].values

# Eğitim-test bölme
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=0, stratify=y
)

# Ölçekleme
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model
model = Sequential()
model.add(Dense(8, kernel_initializer='uniform', activation='relu', input_dim=7))
model.add(Dense(8, kernel_initializer='uniform', activation='relu'))
model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))

# Derleme
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Eğitim
model.fit(X_train, y_train, batch_size=10, epochs=150, verbose=1)

# Tahmin
#model bir değer tahmin eder, bu değer 0.5 den büyükse 1 değilse 0 döndürür
y_pred_prob = model.predict(X_test)
y_pred = (y_pred_prob > 0.5).astype(int)

# Performans
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
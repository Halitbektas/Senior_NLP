import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import precision_score, recall_score, f1_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Veri
#data = load_breast_cancer()
df = pd.read_csv('breast_cancer.csv')
#df = pd.DataFrame(data.data, columns=data.feature_names)
#df["target"] = data.target 

# Girdi ve hedef
X = df.drop("target", axis=1)
y = df["target"]

# Train-test (stratify)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Ölçekleme
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model
model = Sequential([
    Dense(16, activation="relu", input_dim=X_train.shape[1]),
    Dense(8, activation="relu"),
    Dense(1, activation="sigmoid")
])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Eğitim
model.fit(X_train, y_train, epochs=20, batch_size=32, verbose=1, validation_split=0.2)

# Tahmin
#model bir değer tahmin eder, bu değer 0.5 den büyükse 1 değilse 0 döndürür
y_pred = (model.predict(X_test) > 0.5).astype(int)

# Metrikler
print("Accuracy:", model.evaluate(X_test, y_test, verbose=0)[1])
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
#df.to_csv("breast_cancer.csv", index=False)
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import keras
from keras.models import load_model
from keras.models import Sequential

from sklearn.preprocessing import LabelBinarizer


directory = "sign_lang_translator/translator/"

#load train data
train_df = pd.read_csv(f"{directory}asl_dataset/asl_test.csv")
test_df = pd.read_csv(f"{directory}asl_dataset/asl_test.csv")
test = pd.read_csv(f"{directory}asl_dataset/asl_test.csv")
y = test["label"]
train_df.head()


y_train = train_df["label"]
y_test = test_df["label"]
del train_df["label"]
del test_df["label"]

label_binarizer = LabelBinarizer()
y_train = label_binarizer.fit_transform(y_train)
y_test = label_binarizer.fit_transform(y_test)

x_train = train_df.values
x_test = test_df.values

# Normalize the data
x_train = x_train / 255
x_test = x_test / 255

# cnn requires 3 inputs
# reshape data into 3d
x_train = x_train.reshape(-1,28,28,1)
x_test = x_test.reshape(-1,28,28,1)
###

# Load pre trained model
model = load_model(f"{directory}pre_trained/model.h5")
print("Loaded model from disk")

model.compile(loss="binary_crossentropy", optimizer="rmsprop", metrics=["accuracy"])
accuracy = model.evaluate(x_test,y_test)[1]*100
print(f"Accuracy --- {accuracy:.2f}%")

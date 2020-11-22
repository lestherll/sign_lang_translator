import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import keras
from keras.models import load_model
from keras.models import Sequential

from sklearn.preprocessing import LabelBinarizer

# dir to translator folder
directory = "sign_lang_translator/translator/"

# Load pre trained model
model = load_model(f"{directory}pre_trained/perfModel.h5")
print("Loaded model from disk")

# load test data
test_df = pd.read_csv(f"{directory}asl_dataset/asl_test.csv")
test = pd.read_csv(f"{directory}asl_dataset/asl_test.csv")

print(test_df.iloc[0])

# preprocessing
y = test["label"]
y_test = test_df["label"]
del test_df["label"]

label_binarizer = LabelBinarizer()
y_test = label_binarizer.fit_transform(y_test)

# return a numpy representation
x_test = test_df.values

# Normalize the data
x_test = x_test / 255

# reshape data into 3d
x_test = x_test.reshape(-1,28,28,1)
print(x_test)



# compile and test
model.compile(loss="binary_crossentropy", optimizer="rmsprop", metrics=["accuracy"])
accuracy = model.evaluate(x_test,y_test)[1]*100
print(f"Accuracy --- {accuracy:.2f}%")

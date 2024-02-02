#DATASETS IMPORTED FROM KAGGLE.COM

import numpy as np
import cv2

IMAGE_SIZE=(221,221)
IMAGE_FULL_SIZE=(221,221,4)

trainMyImageFolder ="C:\Users\KIIT0001\Downloads\dog-breed-identification.zip\train"

#Now csv file is to be loaded
import pandas as pd
read=pd.read_csv('C:\Users\KIIT0001\Downloads\dog-breed-identification.zip\labels.csv')

print("head of labels:")
print("===============")

print(df.head())
print(df.describe())

print("Group by labels:")
grouplabels=df.groupby("breed")["id"].count()
print(grouplabels.head(10))

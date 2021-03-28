import numpy as np
import pandas as pd

test=pd.read_csv("data/test.csv")
train=pd.read_csv("data/train.csv")

def main():
  data = pd.concat([train,test])
  data.isnull().sum()


main()

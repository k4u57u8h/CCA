import pickle
from sklearn.cluster import KMeans
import numpy as np

with open('mysite\\core\\my_algo.pkl', 'rb') as f:
    kmeans = pickle.load(f)

car = int(input("Do you own a car?(Press 0 if No and Press 1 if Yes): "))
real_estste = int(input("Do you own a House?(Press 0 if No and Press 1 if Yes): "))
income = int(input("Enter your income: "))
print("What is your profession?")
print("0. Commercial Associate")
print("1. Pensioner")
print("2. State Servent")
print("3. Student")
print("4. Working")
profession = int(input("Select your option: "))
print("What is your education level?")
print("0. Academic degree")
print("1. Higher Education")
print("2. Incomplete higher")
print("3. Lower secondary")
print("4. Secondary/Secondary Special")
education = int(input("Select your option: "))

data = np.array([[car, real_estste, income, profession, education]])

answer = kmeans.predict(data)

print(answer)

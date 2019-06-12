import pandas as pd
import numpy as np

from matrixFactorization import matrix_factorization
from createAUI import createAUI
from createAUU import createAUU
from createAII import createAII
from assignComplexValuesAndCreateAMatrix import assignComplexValuesAndCreateAMatrix
from calculateAccuracy import calculateAccuracy

Aui_Train,TestData,xLength,yLength = createAUI()

print("\n User-Item matrisi başarı ile oluşturuldu !")
print(Aui_Train)

AuiTranspose=-(np.transpose(Aui_Train))
print("\n User-Item matrisinin transpozu başarı ile oluşturuldu !")
print(AuiTranspose)
print("\n")

N=xLength
M=yLength

K=5
Steps=5
alpha=0.0002
beta=0.02

P = np.random.rand(N,K)
Q = np.random.rand(M,K)

nP, nQ = matrix_factorization(Aui_Train, P, Q, K, Steps, alpha, beta)
#nR = np.dot(nP, nQ.T)

print("\n Faktorizasyon Islemi Tamamlandi !")

print("\n P = ")
print(nP)		#User 
print("\n Q = ")
print(nQ)		#Item

Auu = createAUU(nP)
print("\n User-User Benzerlik Matrisi Başarı Ile Oluşturuldu !")
print(Auu)
print("\n")

Aii = createAII(nQ)
print("\n Item-Item Benzerlik Matrisi Başarı Ile Oluşturuldu !")
print(Aii)

A = assignComplexValuesAndCreateAMatrix(Aui_Train , AuiTranspose , Auu , Aii , treshold=3)
print("\n Matrisler Tek Bir Matriste Toplandı !")
print(A)

A = A*A*A

print("\n Oluşturulan Matrisin 3.Dereceden Kuvveti Alındı !")
print(A)

print("\n Test Sonuclari : ")
HitRate, Covarage = calculateAccuracy(A,TestData)

print("Hitrate = %" + str(HitRate) + "   Covarage = %" + str(Covarage))


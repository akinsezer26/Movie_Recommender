import numpy as np
from numpy import linalg as LA

def createAII(nQ):

	AII=np.zeros((len(nQ),len(nQ)))
	
	dilim=int(len(nQ)/5)

	for i in range(0,len(nQ)):
		for j in range(0,len(nQ)):
			item1 = nQ[i,:]
			item2 = nQ[j,:]
			AII[i][j] = 1 / (1 +LA.norm(item1 - item2))
		if i % dilim == 0:
			print("Item-Item Benzerlik Matrisi Oluşturuluyor %"+str(i/len(nQ)*100))
	return AII

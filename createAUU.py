import numpy as np
from numpy import linalg as LA

def createAUU(nP):

	AUU=np.zeros((len(nP),len(nP)))

	for i in range(0,len(nP)):
		for j in range(0,len(nP)):
			user1 = nP[i,:]
			user2 = nP[j,:]
			AUU[i][j] = 1 / (1 + LA.norm(user1 - user2))
	return AUU

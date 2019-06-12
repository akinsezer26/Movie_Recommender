import numpy as np

def matrix_factorization(R, P, Q, K, steps, alpha, beta):
	Q = Q.T
	for step in range(steps):
		for i in range(len(R)):
			for j in range(len(R[i])):    
				if R[i][j] > 0:
					try:
						eij = R[i][j] - np.dot(P[i,:],Q[:,j])
					except IndexError:
						print("Oops!  i = ",i,"and len(P) = ",len(P))
						P[i,:]
						break
					for k in range(K):    
						P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])    
						Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])    
		eR = np.dot(P,Q)    
		e = 0    
		for i in range(len(R)):    
			for j in range(len(R[i])):    
				if R[i][j] > 0:                        
					e = e + pow(R[i][j] - np.dot(P[i,:],Q[:,j]), 2)
					for k in range(K):
						e = e + (beta/2) * (pow(P[i][k],2) + pow(Q[k][j],2))    
		if e < 0.001:    
			break   
		print("Faktorizasyon Islemi Yapılıyor %"+str(step/steps*100))
	return P, Q.T

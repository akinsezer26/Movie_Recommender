import numpy as np

def assignComplexValuesAndCreateAMatrix(Aui , AuiTranspose , Auu , Aii , treshold):
	
	UserCount=len(Auu)
	itemCount=len(Aii)

	Aui=Aui.astype(complex)
	AuiTranspose=AuiTranspose.astype(complex)
	Auu=Auu.astype(complex)
	Aii=Aii.astype(complex)

	for i in range(0,len(Aui)):
		for j in range(0,len(Aui[0])):
			if Aui[i][j] == 0:
				Aui[i][j]=0+0j
			elif Aui[i][j]<treshold:
				Aui[i][j]=0-1j
			else:
				Aui[i][j]=0+1j

	for i in range(0,len(AuiTranspose)):
			for j in range(0,len(AuiTranspose[0])):
				if AuiTranspose[i][j] == 0:
					AuiTranspose[i][j]=0+0j
				elif AuiTranspose[i][j]<treshold:
					AuiTranspose[i][j]=0-1j
				else:
					AuiTranspose[i][j]=0+1j

	for i in range(0,len(Auu)):
				for j in range(0,len(Auu[0])):
					if Auu[i][j]<0.5:
						Auu[i][j]=-1+0j
					else:
						Auu[i][j]=1+0j

	for i in range(0,len(Aii)):
				for j in range(0,len(Aii[0])):
					if Aii[i][j]<0.5:
						Aii[i][j]=-1+0j
					else:
						Aii[i][j]=1+0j

	A=np.zeros((UserCount,itemCount),dtype=complex)
	A=np.bmat([[Auu, Aui], [AuiTranspose, Aii]])

	#np.savetxt('A.csv', A , delimiter=',')

	return A

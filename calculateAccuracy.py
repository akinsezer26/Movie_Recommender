import numpy as np

def calculateAccuracy(A,TestData):
	
	Ax=len(A)	#row
	Ay=len(A[0])	#column

	x=len(TestData)	
	y=len(TestData[0])

	sanalKatsayilar=np.zeros((len(TestData),len(TestData[0])),dtype=complex)
	sanalKatsayilar[:][:]=A[(610-x):610,(10352-y):10352]
	sanalKatsayilar=sanalKatsayilar.astype(float)
	sanalKatsayilar=sanalKatsayilar.imag
	
	sanalKatsayilar=sanalKatsayilar.flatten()
	TestData=TestData.flatten()

	missCount=0
	HitCount=0
	CovCount=0
	for i in range(0,len(TestData)):
		if abs(sanalKatsayilar[i]-TestData[i])>2:
			missCount=missCount+1
		elif TestData[i]==0:
			CovCount=CovCount+1
		else:
			HitCount=HitCount+1	
	
	HitRate = HitCount/len(TestData)*100
	Covarage = CovCount/len(TestData)*100
	return HitRate ,Covarage

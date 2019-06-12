import pandas as pd
import numpy as np
def createAUI():
	print("Veriler Çekiliyor ! \n")
	movies = pd.read_csv("movies.csv" , skiprows=0 , usecols=[0])
	ratings = pd.read_csv("ratings.csv" ,skiprows=0 , usecols=[0,1,2])
	movies=np.array(movies)
	ratings=np.array(ratings)

	movieIDMax=0
	for i in range(0,len(ratings)):
		search=ratings[i][1]
		index=np.where(movies==search)
		ratings[i][1]=int(index[0])+1
		if ratings[i][1]>movieIDMax:
			movieIDMax=ratings[i][1]

	xLength=int(ratings[-1][0])
	yLength=int(movieIDMax)
	Aui=np.zeros((xLength , yLength))

	for i in range(0,len(ratings)):
		x=int(ratings[i][0])-1
		y=int(ratings[i][1])-1
		rate=int(ratings[i][2])
		Aui[x][y]=rate
	
	print("Train ve Test Verileri Oluşturuluyor !")

	test=np.zeros((xLength-500,yLength-9000))
	test[:][:] = Aui[500:xLength, 9000:yLength]
	Aui[500:xLength, 9000:yLength] = 0
	train = Aui	
	print(train)

	np.array(train)
	np.array(test)

	#np.savetxt('train.csv', train , delimiter=',')
	#np.savetxt('test.csv', test , delimiter=',')

	return train, test, xLength, yLength

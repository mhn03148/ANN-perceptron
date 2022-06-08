from sklearn.linear_model import Perceptron

X =[[160,55],[163,43],[165,48],[170,80],[175,76],[180,70]]
y = [0,0,0,1,1,1]

clf = Perceptron(tol=1e-3, random_state=0)

clf.fit(X,y)

print(clf.predict(X))
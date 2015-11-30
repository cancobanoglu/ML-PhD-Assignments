__author__ = 'cancobanoglu'
'''
 CCA is Canonical Correlation Analysis
'''

print(__doc__)

from sklearn.cross_decomposition import CCA
from sklearn import datasets

X = [[0., 0., 1.], [1., 0., 0.], [2., 2., 2.], [3., 5., 4.]]
Y = [[0.1, -0.2], [0.9, 1.1], [6.2, 5.9], [11.9, 12.3]]

cca = CCA(n_components=1)
cca.fit(X, Y)

CCA(copy=True, max_iter=500, n_components=1, scale=True, tol=1e-06)

X_c, Y_c = cca.transform(X, Y)

iris = datasets.load_iris()
digits = datasets.load_digits()

print(digits.data)

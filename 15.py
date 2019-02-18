import numpy as np
from scipy.linalg import solve_triangular as solve
from numpy.linalg import inv
from functools import reduce


class Matrix(object):
    def __init__(self, A, b=0):
        """
        creates a matrix and a solution vector for it.
        :param A: The matrix to construct
        :param b: The solution vector by default the vector is a vector of 0's
        """
        self.mat = np.array(A)
        self.b = np.array(0.0 for i in range(len(A))) if b == 0 else np.array(b)

    def __str__(self):
        newstr = ''
        for i in enumerate(self.mat):
            newstr += str(i[1]).replace(']', '|{}]\n'.format(self.b[i[0]]))
        return newstr


    def __str__(self):
        newstr = ''
        for i in enumerate(self.mat):
            newstr += str(i[1]).replace(']', '|{}]\n'.format(self.b[i[0]]))
        return newstr

    @property
    def D(self):
        """
        Defines the diagonal(D) attribute of the matrix
        """
        diag = np.zeros_like(self.mat)
        for i in enumerate(self.mat):
            diag[i[0]][i[0]] = self.mat[i[0]][i[0]]
        return diag

    @property
    def U(self):
        """
        Defines the upper(U) attribute of the matrix
        """
        upper = np.zeros_like(self.mat)
        for i in enumerate(self.mat):
            for j in enumerate(self.mat):
                if i[0] < j[0]:
                    upper[i[0]][j[0]] = self.mat[i[0]][j[0]]
        return upper

    @property
    def L(self):
        """
        Defines the lower(L) attribute of the matrix
        """
        lower = np.zeros_like(self.mat)
        for i in enumerate(self.mat):
            for j in enumerate(self.mat):
                if i[0] > j[0]:
                    lower[i[0]][j[0]] = self.mat[i[0]][j[0]]
        return lower


    def sor(self,w, guess,max_itr=1000,tol=0.00001):
        """
            A variation of Gauss Seidel method that uses a w constant in a a way that would make the
            main diagonal of the matrix a dominant diagonal for faster convention.
            w should be a number between 0 and 2 (not including)
            if w is 1 this methoid is essentially the same as gauss seidel method
            :param w: the constant on which this method is based should be between 0 and 2 not including.
            :param guess: the initial guess for this iterative method
            :param max_itr: max number of tolerable iterations (default 1000)
            :param tol: tolerance of how close the results are
            :return: the solution vector of the Matrix this method is used on.
        """
        if (w<=0 or w>=2):
            return "w out of range"
        a=self.D +w*self.L
        b=w*self.b
        c=w*self.U + (1-w)* self.D
        print ("SOR of this equation list can be represented as:\n{}x={}-{}x".format(a,b,c))
        x = guess
        n = len(self.mat)
        for k in range(max_itr):
            print("iteration number {}:".format(k + 1))
            old_x = x.copy()
            for i in range(n):
                sum1 = 0
                for j in range(i):
                    sum1 += self.mat[i][j] * x[j]
                sum2 = 0
                for j in range(n - 1, i, -1):
                    sum2 += self.mat[i][j] * x[j]
                print("x[{0}] = (1-{5})*x[{0}] ({5}/{1})*({2} - {3} - {4})".format(i + 1, self.mat[i][i], self.b[i], sum1, sum2,w), end="")
                x[i] = (1-w)*x[i] + (w / self.mat[i][i]) * (self.b[i] - sum1 - sum2)
                print(" = {0}".format(x[i]))
            if len(list("ok" for index in range(n) if abs(x[index] - old_x[index])<tol))==n:
                print("took {} iterations".format(k + 1))
                return x
        print("The method didn't converge after {} iterations".format(max_itr))
        return x

B = Matrix([[5,1,10], [10,8,1], [4,10,-5]], (1.5,-7,2))
print(B.sor(1.15,[1,2,3],100))
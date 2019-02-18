def sor(A,b, w=1.25, x0=None, eps=1e-5, max_iteration=100,pItr=0):
    """
    Solves Ax=b
    Parameters
    ----------
    A  : list of list of floats : A matrix
    b : list of list of floats : b vector
    w  : float : weight
    x0 : list of floats : initial guess/None
    eps: float : error size
    max_iteration: int
    pItr : int : print iterations

    Returns
    -------
    list of floats
        solution to the system of linear equation

    Raises
    ------
    ValueError
        Solution does not converge
    """
    for i in range(len(A)):
        A[i].append(b[i][0])
    m=A
    n = len(m)
    x0 = [0] * n if x0 == None else x0
    x1 = x0[:]
    itr=0
    for __ in range(max_iteration):
        for i in range(n):
            s = sum(-m[i][j] * x1[j] for j in range(n) if i != j)
            x1[i] = w * (m[i][n] + s) / m[i][i] + (1 - w) * x0[i]
            itr+=1
            if(pItr==1):
                print("X[",itr,"]=",x1)
        if all(abs(x1[i] - x0[i]) < eps for i in range(n)):
            return x1
        x0 = x1[:]
    raise ValueError('Solution does not converge')

A = [[5,1,10], [10,8,1], [4,10,-5]]
b=[[1.5],[-7],[2]]
#print without iterations of Xi
print("Vector x of Ax=b: ",sor(A,b,1.15))
#print with iterations of Xi
print("Vector x of Ax=b: ",sor(A,b,pItr=1))
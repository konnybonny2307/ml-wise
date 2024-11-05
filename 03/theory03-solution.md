# Exercise 1

## (a)

The optimization problem is given by 

$`
 \arg \max_{u} \frac{1}{N} \sum_{i=1}^N \left( u^{\top} (x_i - m) \right)^2 \quad \text{subject to} \quad \|u\|^2 = 1, 
`$
where $` m = \frac{1}{N} \sum_{i=1}^N x_i `$ is the mean of the data points $` x_i \in \mathbb{R}^d `$.

Assuming the data is centered, we set $` m = 0 `$, which simplifies the expression to

$`
\arg \max_{u} \frac{1}{N} \sum_{i=1}^N \left( u^{\top} x_i \right)^2 \quad \text{subject to} \quad \|u\|^2 = 1.
`$

We can expand $` \left( u^{\top} x_i \right)^2 `$ as follows:

$`
\frac{1}{N} \sum_{i=1}^N \left( u^{\top} x_i \right)^2 = \frac{1}{N} \sum_{i=1}^N \left( u^{\top} x_i \right) \left( x_i^{\top} u \right).
`$

This can be rewritten as

$`
= u^{\top} \left( \frac{1}{N} \sum_{i=1}^N x_i x_i^{\top} \right) u.
`$

Define the covariance matrix $` \Sigma `$ as

$`
\Sigma = \frac{1}{N} \sum_{i=1}^N (x_i - m)(x_i - m)^{\top}.
`$

Since $` m = 0 `$, we have

$`
\Sigma = \frac{1}{N} \sum_{i=1}^N x_i x_i^{\top}.
`$

Thus, the optimization problem becomes

$`
\arg \max_{u} u^{\top} \Sigma u \quad \text{subject to} \quad \|u\|^2 = 1.
`$

## (b)

Firstly we construct Lagrangian function:

$`
\mathcal{L}(u, \lambda) = u^{\top} \Sigma u - \lambda \left( u^{\top} u - 1 \right).
`$

To find the stationary points, we take the derivative of $` \mathcal{L} `$ with respect to $` u `$ and set it to zero:

$`
\nabla_u \mathcal{L}(u, \lambda) = 2 \Sigma u - 2 \lambda u = 0.
`$

This simplifies to

$`
\Sigma u = \lambda u.
`$

# Exercise 2

## a)

The Relation easily comes from the trace and the equalities from the lecture:

$`\sum_{i=1}^{d} \Sigma `$
$`= Tr( \Sigma ) = \sum_{k=1}^{d} \lambda_i > \lambda_1`$

## b) 

We can express the covariance matrix $` \Sigma `$ in therm of its eigenvalues and eigenvectors as:

$` \Sigma = \sum_{i=1}^d \lambda_k u_k u_k^{\top} ,`$

where $` u_k `$ is the eigenvector associated with the eigenvalue $` \lambda_k `$

Each $` \Sigma_{ii} `$ can be expressed as:

$` \Sigma_{ii} = \sum_{k=1}^d \lambda_k (u_k)_i^2 .`$

Since $` \lambda_{1} > \lambda_k `$ for all $` k = 1 `$:

$` \Sigma_{ii} \le \lambda_{1} \sum_{k=1}^d (u_k)_i^2 `$

with

$´ \sum_{k=1}^d (u_k)_i^2 = 1 `$ 

it simplyfies to

$` \Sigma_{ii} \le \lambda_{1} .`$

Since it is true for all $´ i `$, we find that:

$` max_{i=1}^d \Sigma \le \lambda_{1}`$ 

# Exercise 3

## a) 

Consider $w$ for step $t+1$ in $\varepsilon_k$: 

$\varepsilon_k(w^{(t+1)}) = |\frac{w^{(t+1)^\top} u_k}{w^{(t+1)^\top}u_1}| = |\frac{(\sum w^{(t+1)})^\top u_k}{(\sum w^{(t+1)})^\top u_1}| = |\frac{( w^{(t+1)}\sum)^\top u_k}{(w^{(t+1)}\sum)^\top u_1}| = |\frac{(w^t)^\top\sum u_k}{(w^t)^\top\sum u_1}| $

We can swap **∑** and $w_k$ because correlation matrix is symmetric.

## b)

$\varepsilon_k(w^{(t+1)}) = |\frac{(w^t)^\top\sum u_k}{ (w^t)^\top\sum u_1}| = |\frac{(w^t)^\top\lambda_ku_k}{ (w^t)^\top\lambda_1 u_1}| = |\frac{\lambda_k}{\lambda_1}||\frac{(w^t)^\top u_k}{ (w^t)^\top u_1}| =  |\frac{\lambda_k}{\lambda_1}|\varepsilon_k(w^t)$
 
## c)

From our recurrence, this gives us: 

$\varepsilon_k(w^{(t)}) = |\frac{\lambda_k}{\lambda_1}|\varepsilon_k(w^{(t-1)}) = |(\frac{\lambda_k}{\lambda_1})^2|\varepsilon_k(w^{(t-2)}) = |(\frac{\lambda_k}{\lambda_1})^t|\varepsilon_k(w^{(0)})$
### Exercise 1

## (a)

The optimization problem is given by
$$
\arg \max_{u} \frac{1}{N} \sum_{i=1}^N \left( u^{\top} (x_i - m) \right)^2 \quad \text{subject to} \quad \|u\|^2 = 1,
$$
where $ m = \frac{1}{N} \sum_{i=1}^N x_i $ is the mean of the data points $ x_i \in \mathbb{R}^d $.

\paragraph{Step 1: Centering the Data}

Assuming the data is centered, we set $ m = 0 $, which simplifies the expression to
$$
\arg \max_{u} \frac{1}{N} \sum_{i=1}^N \left( u^{\top} x_i \right)^2 \quad \text{subject to} \quad \|u\|^2 = 1.
$$

\paragraph{Step 2: Expanding the Objective Function}

We can expand $ \left( u^{\top} x_i \right)^2 $ as follows:
$$
\frac{1}{N} \sum_{i=1}^N \left( u^{\top} x_i \right)^2 = \frac{1}{N} \sum_{i=1}^N \left( u^{\top} x_i \right) \left( x_i^{\top} u \right).
$$
This can be rewritten as
$$
= u^{\top} \left( \frac{1}{N} \sum_{i=1}^N x_i x_i^{\top} \right) u.
$$

\paragraph{Step 3: Recognizing the Covariance Matrix}

Define the covariance matrix $ \Sigma $ as
$$
\Sigma = \frac{1}{N} \sum_{i=1}^N (x_i - m)(x_i - m)^{\top}.
$$
Since $ m = 0 $, we have
$$
\Sigma = \frac{1}{N} \sum_{i=1}^N x_i x_i^{\top}.
$$
Thus, the optimization problem becomes
$$
\arg \max_{u} u^{\top} \Sigma u \quad \text{subject to} \quad \|u\|^2 = 1.
$$

## (b)

To solve this maximization problem with the constraint $ \|u\|^2 = 1 $, we use the method of Lagrange multipliers.

\paragraph{Step 1: Define the Lagrangian}

Construct the Lagrangian function:
$$
\mathcal{L}(u, \lambda) = u^{\top} \Sigma u - \lambda \left( u^{\top} u - 1 \right).
$$

\paragraph{Step 2: Take the Gradient with Respect to $ u $}

To find the stationary points, take the derivative of $ \mathcal{L} $ with respect to $ u $ and set it to zero:
$$
\nabla_u \mathcal{L}(u, \lambda) = 2 \Sigma u - 2 \lambda u = 0.
$$
This simplifies to
$$
\Sigma u = \lambda u.
$$
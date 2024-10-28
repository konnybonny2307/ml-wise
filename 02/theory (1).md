## Exercise 1

### (a)

We start by expanding the function of \( y \) as follows: 
\[
y(x, x') = ||x - x'||^{2} = \sum_{t = 1}^{d}(x_t - x'_t)^{2}
\]

Since \( x \sim N(0, I) \) where \( I \) is the identity matrix, we can express this as \( x \sim N(0,1) \) for each component.  
Let \( z = x - x' \). Then \( z \sim N(0,1) - N(0,1) \sim N(0,2) \), because \( x \) and \( x' \) were drawn independently.

For the second moment of the normal distribution, we have:
\[
\mathbb{E}[(x_i - x'_i)^2] = \mathbb{E}[z^2] = \mu^2 + \sigma^2 = 2
\]
Thus, we conclude that the mean function \( \mu \) satisfies:
\[
\mathbb{E}[y] = \mathbb{E}\left[\sum_{i=1}^{d} (x_i - x'_i)^2\right] = \sum_{i=1}^{d} \mathbb{E}[(x_i - x'_i)^2] = 2d
\]
by linearity.

### (b)

Since \( X_i \) is independent of \( X_j \) for \( i \neq j \), it holds that:
\[
\operatorname{Var}\left[\sum X_i\right] = \sum \operatorname{Var}[X_i] = d \operatorname{Var}[X_i]
\]
Note that in general, \( \operatorname{Var}[X_i] = \mathbb{E}[X_i^2] - \mathbb{E}[X_i]^2 \).

Given that \( z \sim N(0,2) \), we observe that:
\[
\mathbb{E}[X_i^2] = \mathbb{E}[(x_i - x'_i)^4] = \mathbb{E}[z^4] = 3\sigma^4 = 8
\]

Thus, we get:
\[
\operatorname{Var}[y] = \operatorname{Var}\left[\sum X_i\right] = 8d \quad \text{and} \quad \operatorname{std}[y] = \sqrt{8d}
\]

### (c)

From (a) and (b), we have:
\[
\frac{\operatorname{std}[y]}{\mathbb{E}[y]} = \frac{\sqrt{8d}}{2d} = \sqrt{\frac{2}{d}}
\]
If we set \( d = 2 \), we find:
\[
\frac{\sqrt{8d}}{2d} = \frac{4}{4} = \sqrt{\frac{2}{d}} = \sqrt{\frac{2}{2}}
\]

Therefore, as \( d \) grows, square distances concentrate more, confirming that the concentration effect increases with \( d \).

import numpy as np
from scipy.optimize import minimize

# Observed data
X = np.array([2, 1, 3, 0, 4, 2, 1, 3, 2, 5])

# Log-likelihood function for Poisson distribution
def neg_log_likelihood(lmbda, x):
    return -np.sum(np.log(np.exp(-lmbda) * (lmbda ** x) / np.math.factorial(x)))

# Find MLE for lambda
result = minimize(neg_log_likelihood, x0=1, args=(X,), method='BFGS')
mle_lambda = result.x[0]

print(f"Maximum Likelihood Estimator (MLE) for lambda: {mle_lambda}")

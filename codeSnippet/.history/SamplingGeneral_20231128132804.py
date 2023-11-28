In general we can write a pthon code for sampling from different distribution
\begin{python}
import numpy as np

class DistributionSampler:
    def __init__(self, distribution, params=None):
        """
        Initialize the DistributionSampler.

        Parameters:
        - distribution: A function representing the distribution to sample from.
        - params: Parameters specific to the distribution function.
        """
        self.distribution = distribution
        self.params = params

    def sample(self, num_samples, sample_size):
        """
        Generate samples from the specified distribution.

        Parameters:
        - num_samples: The number of samples to generate.
        - sample_size: The size of each sample.

        Returns:
        A tuple containing the means and variances of the samples.
        """
        samples = np.zeros((num_samples, sample_size))
        means = np.zeros((num_samples, sample_size))
        variances = np.zeros((num_samples, sample_size))

        for i in range(num_samples):
            for j in range(sample_size):
                samp = self.distribution(size=j + 1, params=self.params)
                samples[i, j] = np.mean(samp)
                means[i, j] = np.mean(samp)
                variances[i, j] = np.var(samp)

        return means, variances


def normal_distribution(size, params):
    """
    Generate samples from a normal distribution.

    Parameters:
    - size: The size of the sample.
    - params: Parameters specific to the normal distribution (mean, standard deviation).

    Returns:
    An array of samples from the normal distribution.
    """
    return np.random.normal(loc=params['mean'], scale=params['std'], size=size)


# Example usage:
pop_params = {'mean': 85, 'std': 5}
num_samples = 10
sample_size = 15

sampler = DistributionSampler(normal_distribution, params=pop_params)
means, variances = sampler.sample(num_samples, sample_size)

# Display 15 data points of means and variances
for k in range(15):
    print(f"Sample Size: {k + 1}")
    print("Means:", means[:15, k])
    print("Variances:", variances[:15, k])
    print("-" * 40)
In general we can write a pthon code for sampling from different distribution
\begin{python}
import numpy as np

class DistributionSampler:
    def __init__(self, distribution, params=None):
        """
        Initialize the DistributionSampler.

        Parameters:
        - distribution: A function representing the distribution to sample from.
        - params: Parameters specific to the distribution function.
        """
        self.distribution = distribution
        self.params = params

    def sample(self, num_samples, sample_size):
        """
        Generate samples from the specified distribution.

        Parameters:
        - num_samples: The number of samples to generate.
        - sample_size: The size of each sample.

        Returns:
        A tuple containing the means and variances of the samples.
        """
        samples = np.zeros((num_samples, sample_size))
        means = np.zeros((num_samples, sample_size))
        variances = np.zeros((num_samples, sample_size))

        for i in range(num_samples):
            for j in range(sample_size):
                samp = self.distribution(size=j + 1, params=self.params)
                samples[i, j] = np.mean(samp)
                means[i, j] = np.mean(samp)
                variances[i, j] = np.var(samp)

        return means, variances


def normal_distribution(size, params):
    """
    Generate samples from a normal distribution.

    Parameters:
    - size: The size of the sample.
    - params: Parameters specific to the normal distribution (mean, standard deviation).

    Returns:
    An array of samples from the normal distribution.
    """
    return np.random.normal(loc=params['mean'], scale=params['std'], size=size)


# Example usage:
pop_params = {'mean': 85, 'std': 5}
num_samples = 10
sample_size = 15

sampler = DistributionSampler(normal_distribution, params=pop_params)
means, variances = sampler.sample(num_samples, sample_size)

# Display 15 data points of means and variances
for k in range(15):
    print(f"Sample Size: {k + 1}")
    print("Means:", means[:15, k])
    print("Variances:", variances[:15, k])
    print("-" * 40)

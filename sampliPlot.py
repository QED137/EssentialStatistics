import numpy as np

# Assuming you have a population 'pop'
pop = np.random.randint(70, 100, size=10)
print(pop)
num_samples = 10
sample_size = 15

sampmean = np.zeros((num_samples, sample_size))
sampvar = np.zeros((num_samples, sample_size))

for i in range(num_samples):
    for j in range(sample_size):
        samp = np.random.choice(pop, size=j+1, replace=True)
        sampmean[i, j] = np.mean(samp)
        sampvar[i, j] = np.var(samp)

# Display 15 data points of means and variances
for k in range(15):
    print(f"Sample Size: {k+1}")
    print("Means:", sampmean[:15, k])
    print("Variances:", sampvar[:15, k])
    print("-" * 40)
auto
from scipy.optimize import curve_fit

# Load the Facebook data
data = pd.read_csv('Facebook.csv', delimiter='\t', usecols=range(3))

# Define the Metcalfe utility function
def metcalfe_utility(x, a):
    return a * x * (x - 1) / 2

# Fit the Metcalfe utility function to the data
popt, pcov = curve_fit(metcalfe_utility, data['MAU'], data['Total Assets'])

# Get the value of the scaling coefficient
a = popt[0]

# Get the value of the exponent
exponent = 1 - 1 / a

if exponent > 1/2:
    print("The marginal utility of the value of Facebook decreases as the value of Facebook increases.")
elif exponent < 1/2:
    print("The marginal utility of the value of Facebook increases as the value of Facebook increases.")
else:
    print("The marginal utility of the value of Facebook is constant.")

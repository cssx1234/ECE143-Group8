import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

def humidity_correlation(csv_file_path):
    """
    Read a CSV file containing cleaned F1 merged data into a Pandas DataFrame.
    Calculate the correlation coefficient between Humidity and Points earned by each driver.
    Plot the correlation coefficients as a bar graph.

    Parameters:
    - csv_file_path (str): The path to the cleaned CSV file.

    Returns:
    - None
    """

    assert isinstance(csv_file_path, str), "input must be a file path string"

    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Calculate correlation coefficient for each driver
    drivers = df['driverCode'].unique()

    correlation_coefficients = []

    for driver in drivers:
        driver_data = df[df['driverCode'] == driver]

        # Calculate correlation coefficient
        correlation_coefficient, _ = pearsonr(driver_data['Humidity'], driver_data['points'])

        correlation_coefficients.append(correlation_coefficient)

    # Plot correlation coefficients as a bar graph
    plt.bar(drivers, correlation_coefficients, color="black")
    plt.xlabel('Driver')
    plt.ylabel('Correlation Coefficient')
    plt.title('Corr. Coeff. Between Humidity (%) and Points Earned by Each Driver')
    plt.show()

csv_file_path = 'cleaned_f1_merged_data.csv'
# Call the function with the cleaned CSV file path
humidity_correlation(csv_file_path)

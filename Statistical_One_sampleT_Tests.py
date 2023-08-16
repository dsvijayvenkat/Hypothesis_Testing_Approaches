import pandas as pd
import numpy as np
from scipy import stats 

def perform_one_sample_t_test(data, column_name, population_mean):
    one_sample_data = data[column_name]
    
    t_statistic, p_value = stats.ttest_1samp(one_sample_data, population_mean)
    
    print("*" * 40)
    print("One-Sample T-Test:")
    print("t-statistic:", t_statistic)
    print("p-value:", p_value)
    
    if p_value < 0.05:
        print("Reject Null Hypothesis")
    else:
        print("Fail to Reject Null Hypothesis")
    
    print("*" * 40)

if __name__ == "__main__":
    data = pd.read_csv(r"C:\Users\venka\OneDrive\Documents\Datasets\bank_dataset.csv")
    
    cal_population_mean = data["age"].mean()
    population_mean = 40.014  # Adjust this value based on your data
    perform_one_sample_t_test(data, 'age', population_mean)
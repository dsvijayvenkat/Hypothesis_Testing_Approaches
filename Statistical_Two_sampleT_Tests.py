import pandas as pd
import numpy as np
from scipy import stats 

def perform_two_sample_t_test(data, column_name, group_A_filter, group_B_filter):
    group_A = data[group_A_filter][column_name]  # Corrected this line
    group_B = data[group_B_filter][column_name]  # Corrected this line
    
    t_statistic, p_value = stats.ttest_ind(group_A, group_B)
    
    print("*" * 40)
    print("Two-Sample T-Test:")
    print("t-statistic:", t_statistic)
    print("p-value:", p_value)
    
    if p_value < 0.05:
        print("Reject Null Hypothesis")
    else:
        print("Fail to Reject Null Hypothesis")
    
    print("*" * 40)

if __name__ == "__main__":
    data = pd.read_csv(r"C:\Users\venka\OneDrive\Documents\Datasets\bank_dataset.csv")
    
    perform_two_sample_t_test(data, 'balance', data['loan'] == 'no', data['loan'] == 'yes')

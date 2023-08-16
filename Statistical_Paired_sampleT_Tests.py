import pandas as pd
import numpy as np
from scipy import stats 

def perform_paired_sample_t_test(data, column_name_pre, column_name_post):
    pre_test = data[column_name_pre]
    post_test = data[column_name_post]
    
    t_statistic, p_value = stats.ttest_rel(post_test, pre_test)
    
    print("*" * 40)
    print("Paired Sample T-Test:")
    print("t-statistic:", t_statistic)
    print("p-value:", p_value)
    
    if p_value < 0.05:
        print("Reject Null Hypothesis")
    else:
        print("Fail to Reject Null Hypothesis")
    
    print("*" * 40)

if __name__ == "__main__":
    data = pd.read_csv(r"C:\Users\venka\OneDrive\Documents\Datasets\bank_dataset.csv")
    
    perform_paired_sample_t_test(data, 'previous', 'campaign')

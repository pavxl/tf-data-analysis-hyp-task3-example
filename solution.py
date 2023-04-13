import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 362844815

def solution(x, y) -> bool:
    p_value = ttest_ind(x, y, alternative="greater").pvalue
    return p_value < 0.03

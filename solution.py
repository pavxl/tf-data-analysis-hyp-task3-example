import pandas as pd
import numpy as np
from scipy.stats import cramervonmises_2samp

chat_id = 362844815

def solution(x: np.array, y: np.array) -> bool:
    result = cramervonmises_2samp(x, y)
    statistic, pvalue = result.statistic, result.pvalue
    alpha = 0.01
    if pvalue > alpha:
        return True
    else:
        return False

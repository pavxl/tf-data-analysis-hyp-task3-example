import pandas as pd
import numpy as np
import statsmodels.stats.weightstats as ws

chat_id = 362844815

def solution(x: np.array, y: np.array) -> bool:
    _, pvalue = ws.ztest(x, value=500, alternative='larger')

    return pvalue <= 0.03

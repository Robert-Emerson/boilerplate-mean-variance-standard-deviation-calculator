import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    np_array = np.array(list)
    np_array = np_array.reshape(3,3)

    calculations = {}

    calculations["mean"] = calculate_mean(np_array)
    calculations["variance"] = calculate_variance(np_array)
    calculations["standard deviation"] = calculate_std(np_array)
    calculations["max"] = calculate_max(np_array)
    calculations["min"] = calculate_min(np_array)
    calculations["sum"] = calculate_sum(np_array)

    return calculations

def calculate_mean(np_array) -> []:
    return [list(np.mean(np_array,axis=0)), list(np.mean(np_array,axis=1)), np.mean(np_array)]

def calculate_variance(np_array) -> []:
    return [list(np.var(np_array,axis=0)), list(np.var(np_array,axis=1)), np.var(np_array)]

def calculate_std(np_array) -> []:
    return [list(np.std(np_array,axis=0)), list(np.std(np_array,axis=1)), np.std(np_array)]

def calculate_max(np_array) -> []:
    return [list(np.max(np_array,axis=0)), list(np.max(np_array,axis=1)), np.max(np_array)]

def calculate_min(np_array) -> []:
    return [list(np.min(np_array,axis=0)), list(np.min(np_array,axis=1)), np.min(np_array)]

def calculate_sum(np_array) -> []:
    return [list(np.sum(np_array,axis=0)), list(np.sum(np_array,axis=1)), np.sum(np_array)]
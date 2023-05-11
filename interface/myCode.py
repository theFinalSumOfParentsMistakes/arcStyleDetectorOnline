import pandas as pd
import os
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

PATH = '/Users/d.s.zubov/Desktop/Курсовая работа/Код/MyDiploma/sheet/Resource'


def compare_halves(arr, current_depth, max_depth):
    n = len(arr)
    if n == 1:
        return [0]
    elif n == 2:
        if arr[0] > arr[1]:
            return [1]
        else:
            return [0]
    elif current_depth > max_depth:
        return []
    else:
        center = n // 2
        left_sum = sum(arr[:center])
        right_sum = sum(arr[center:])
        if left_sum > right_sum:
            return compare_halves(arr[:center],current_depth+1, max_depth) + [1] + compare_halves(arr[center:],current_depth+1, max_depth)
        else:
            return compare_halves(arr[:center],current_depth+1, max_depth) + [0] + compare_halves(arr[center:],current_depth+1, max_depth)


def matrix_to_array(matrix):
    matrix = np.array(matrix)
    array = []
    r = matrix.shape[0]
    for i in range(-r+1,r):
        array = np.concatenate((array,np.diag(matrix,i)),axis=None)
    return array

def levinshtein_distance(source_str, target_str):
    distance = 0
    distance += abs(len(source_str) - len(target_str))
    for i in range(min(len(source_str), len(target_str))):
        if source_str[i] != target_str[i]:
            distance +=1
    return distance


def model(test_object, dataset_learn: pd.DataFrame, k):
    dataset_learn['distance'] = dataset_learn["array"].apply(lambda x: levinshtein_distance(test_object, x))
    sorted_data = dataset_learn.sort_values(['distance'])
    style = sorted_data[:k].groupby('style').count().sort_values(['distance'], ascending=False).index[0]
    return style, sorted_data[:5]



img = Image.open('./static/Russian_Revival_25.jpg')
img_array = compare_halves(matrix_to_array(img), current_depth=0, max_depth=12)
data = pd.read_csv('./static/database.csv', sep=';')
print(model(img_array, data, 2)[0])
top = model(img_array, data, 2)[1]
l = 4

fig = plt.figure(figsize=(30, 30))
for x in range(2):
    for i in range(l):
        ax = fig.add_subplot(10, l, i+1)
        plt.imshow(Image.open(f'./static/files/data{(list(top.path)[i])[8:]}'), cmap='gray')
        plt.title(list(top['style'])[i])


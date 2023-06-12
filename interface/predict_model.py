import pandas as pd
import os
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

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

STATIC_PATH = './interface/static/'

def model(size, d, k, num_resp_imgs, database_name ):
    test_object = Image.open(f'{STATIC_PATH}taked_photo.jpg')
    size_div_2 = size
    # предобработка
    image = test_object.convert('L')
    image_center = (image.size[0] // 2, image.size[1] // 2)
    crop_1 = (image_center[0] - size_div_2, image_center[1] - size_div_2, image_center[0] + size_div_2, image_center[1] + size_div_2)
    image = image.crop(crop_1)
    # работа модели
    img_array = compare_halves(matrix_to_array(image), current_depth=0, max_depth=d)
    data = pd.read_csv(f'{STATIC_PATH}{database_name}', sep=';')

    data['distance'] = data['array'].apply(
        lambda x: int(levinshtein_distance(str(img_array), str(x))))
    dataset_learn_sorted = data.sort_values(by='distance')
    dataset_learn_sorted_grouped = dataset_learn_sorted[:k].groupby('style').count().sort_values(by='distance',
                                                                                                 ascending=False)
    style = dataset_learn_sorted_grouped.index[0]

    # data['distance'] = data["array"].apply(lambda x: levinshtein_distance(img_array, x))
    # sorted_data = data.sort_values(['distance'])
    # style = sorted_data[:50].groupby('style').count().sort_values(['distance'], ascending=False).index[0]
    imgs = dataset_learn_sorted["path"][:num_resp_imgs].apply(lambda s: 'files/'+s[9:])
    return style, imgs.tolist()

#
# s = './data_d/Russian Revival/Russian_Revival_19.jpg'
#
# print('files/data/'+s[9:])

# fig = plt.figure(figsize=(30, 30))
# for x in range(2):
#     for i in range(l):
#         ax = fig.add_subplot(10, l, i+1)
#         plt.imshow(Image.open(list(top.path)[i]), cmap='gray')
#         plt.title(list(top['style'])[i])
#

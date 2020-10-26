# 专事专办
import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel, BertForMaskedLM

import os
import json
import numpy as np


def bert_precessing(text):
    tokenizer = BertTokenizer.from_pretrained('uncased_L-2_H-128_A-2')
    tokenized_text = tokenizer.tokenize(text)
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)

    segments_ids = [1] * len(tokenized_text)
    # Convert inputs to PyTorch tensors
    tokens_tensor = torch.tensor([indexed_tokens])
    segments_tensors = torch.tensor([segments_ids])
    # Load pre-trained model (weights)
    model = BertModel.from_pretrained('uncased_L-2_H-128_A-2')
    # Put the model in "evaluation" mode, meaning feed-forward operation.
    model.eval()

    with torch.no_grad():
        encoded_layers, _ = model(tokens_tensor, segments_tensors)

    text_vector = np.zeros(128, dtype=float)
    for each_word_vector in encoded_layers[-1][0]:
        text_vector += each_word_vector.cpu().detach().numpy()
    return text_vector


def normalization(vector):
    max_value = np.max(vector)
    min_value = np.min(vector)
    return (vector - min_value) / (max_value - min_value)


if __name__ == '__main__':
    json_read_file_path = '词向量预处理数据_2/yjm_20201023.json'

    made_text_list = json.load(open(json_read_file_path, 'r', encoding='UTF-8'))
    text_matrix = np.zeros((len(made_text_list), 128))
    for i in range(len(made_text_list)):
        print(i)
        text_vector = bert_precessing(made_text_list[i])
        # 归一化
        text_vector = normalization(text_vector)
        text_matrix[i] = text_vector
    print(text_matrix)

    np.save('text_matrix', text_matrix)

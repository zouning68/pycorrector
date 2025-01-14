# -*- coding: utf-8 -*-
# Author: XuMing <xuming624@qq.com>
# Brief:
import os

pwd_path = os.path.abspath(os.path.dirname(__file__))

# CGED chinese corpus
raw_train_paths = [
    os.path.join(pwd_path, '../data/cn/CGED/CGED18_HSK_TrainingSet.xml'),
    os.path.join(pwd_path, '../data/cn/CGED/CGED17_HSK_TrainingSet.xml'),
    os.path.join(pwd_path, '../data/cn/CGED/CGED16_HSK_TrainingSet.xml'),
    # os.path.join(pwd_path, '../data/cn/CGED/sample_HSK_TrainingSet.xml'),
]

output_dir = os.path.join(pwd_path, 'output')
train_word_path = output_dir + '/train_words.txt'
train_label_path = output_dir + '/train_labels.txt'
test_paths = {
    os.path.join(pwd_path, '../data/cn/CGED/CGED16_HSK_Test_Input.txt'):
        os.path.join(pwd_path, '../data/cn/CGED/CGED16_HSK_Test_Truth.txt'),
    os.path.join(pwd_path, '../data/cn/CGED/CGED17_HSK_Test_Input.txt'):
        os.path.join(pwd_path, '../data/cn/CGED/CGED17_HSK_Test_Truth.txt'),
    # os.path.join(pwd_path, '../data/cn/CGED/sample_HSK_Test_Input.txt'):
    #     os.path.join(pwd_path, '../data/cn/CGED/sample_HSK_Test_Truth.txt'),
}
test_word_path = output_dir + '/test_words.txt'
test_label_path = output_dir + '/test_labels.txt'
test_id_path = output_dir + '/test_ids.txt'
# vocab
word_dict_path = output_dir + '/word_freq.txt'
label_dict_path = output_dir + '/label_dict.txt'

# config
batch_size = 64
epoch = 10
embedding_dim = 100
rnn_hidden_dim = 200
maxlen = 300
cutoff_frequency = 5
dropout = 0.25
save_model_path = output_dir + '/rnn_crf_model.h5'  # Path of the model saved, default is output_path/model

# infer
save_pred_path = output_dir + '/pred.txt'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

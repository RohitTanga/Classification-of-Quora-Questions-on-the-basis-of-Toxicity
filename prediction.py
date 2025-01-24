import numpy as np
from transformers import AutoTokenizer
from tensorflow import keras
from keras.models import load_model
import tensorflow_hub as tfhb
from keras.utils import custom_object_scope
import tensorflow as tf
class md():
    with custom_object_scope({'KerasLayer': tfhb.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/2",trainable=False)}):                                
        model=load_model("Finetuning-BERT-For-classification-of-text\model\model.h5")
    tokenizer=AutoTokenizer.from_pretrained('bert-base-uncased')
    def __init__(self):
        self.max_seq_length=128
    def predict(self,text):
        x=md.tokenizer(text,max_length=self.max_seq_length,padding='max_length',truncation=True,add_special_tokens=True)
        y={}
        y['input_word_ids']=np.array(x['input_ids']).reshape(1,128)
        y['input_mask']=np.array(x['attention_mask']).reshape(1,128)
        y['input_type_ids']=np.array(x['token_type_ids']).reshape(1,128)
        pred=tf.data.Dataset.from_tensor_slices((y)).batch(1)
        k=md.model.predict(pred)
        print(k)
        threshold=0.0001
        if threshold<k[0][0]:
            return 1#insincere
        else:
            return 0#sincere
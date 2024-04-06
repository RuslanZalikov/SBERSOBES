import torch

from transformers import BertTokenizerFast
from transformers import AutoModelForSequenceClassification


tokenizer = BertTokenizerFast.from_pretrained('blanchefort/rubert-base-cased-sentiment-rusentiment')
model = AutoModelForSequenceClassification.from_pretrained('blanchefort/rubert-base-cased-sentiment-rusentiment', return_dict=True)

tokenizer.save_pretrained("./save_model/tokenizer/" )
model.save_pretrained("./save_model/model/")

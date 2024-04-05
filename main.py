import torch
from transformers import AutoModelForSequenceClassification
from transformers import BertTokenizerFast

tokenizer = BertTokenizerFast.from_pretrained('blanchefort/rubert-base-cased-sentiment-rusentiment')
model = AutoModelForSequenceClassification.from_pretrained('blanchefort/rubert-base-cased-sentiment-rusentiment')

tokenizer.save_pretrained("./save_model/" )
torch.save(model.state_dict(), './save_model/pytorch_model.bin')

# model2 = torch.load('./save_model/model.safetensors')
# tokenizer2 = torch.load("./save_model/")

# print(tokenizer2)
# print(model2)
# def predict(text):
#     inputs = tokenizer2(text, max_length=512, padding=True, truncation=True, return_tensors='pt')
#     outputs = model2(**inputs)
#     predicted = torch.nn.functional.softmax(outputs.logits, dim=1)
#     predicted = torch.argmax(predicted, dim=1).numpy()
#     return predicted
#
# print(predict("Глупый"))
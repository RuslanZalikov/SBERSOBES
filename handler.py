from ts.torch_handler.text_handler import TextHandler
from transformers import AutoModelForSequenceClassification
from transformers import BertTokenizerFast
import torch

class Handler(TextHandler):
    def __init__(self):
        super().__init__()
        self.model = None
        self.tokenizer = None

    def initialize(self, context):
        self.model = AutoModelForSequenceClassification.from_pretrained("./save_model/pytorch_model.bin")
        self.tokenizer = BertTokenizerFast.from_pretrained("./save_model/")

    def preprocess(self, data):
        preprocessed_data = data[0].get("data")
        if preprocessed_data is None:
            preprocessed_data = data[0].get("body")

        return preprocessed_data

    def inference(self, data, *args, **kwargs):
        inputs = self.tokenizer(data, max_length=512, padding=True, truncation=True, return_tensors='pt')
        outputs = self.model(**inputs)
        predicted = torch.nn.functional.softmax(outputs.logits, dim=1)
        predicted = torch.argmax(predicted, dim=1).numpy()
        return predicted

    def postprocess(self, data):
        return data
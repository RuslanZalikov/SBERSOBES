import json
import torch

from transformers import BertConfig
from transformers import BertTokenizerFast
from transformers import AutoModelForSequenceClassification

from ts.torch_handler.text_handler import TextHandler


class Handler(TextHandler):
    def __init__(self):
        super().__init__()
        self.model = None
        self.tokenizer = None
        self.config = None

    def initialize(self, context):
        self.tokenizer = BertTokenizerFast.from_pretrained("/code/save_model/tokenizer/", local_files_only=True)
        self.config = BertConfig.from_pretrained(f"/code/save_model/model", local_files_only=True)
        self.model = AutoModelForSequenceClassification.from_config(self.config)


    def preprocess(self, data):
        preprocessed_data = data[0].get("data")
        if preprocessed_data is None:
            preprocessed_data = data[0].get("body")
        return preprocessed_data if isinstance(preprocessed_data, str) else preprocessed_data.decode("utf-8")

    def inference(self, data, *args, **kwargs):
        inputs = self.tokenizer(data, max_length=512, padding=True, truncation=True, return_tensors='pt')
        outputs = self.model(**inputs)
        predicted = torch.nn.functional.softmax(outputs.logits, dim=1)
        predicted = torch.argmax(predicted, dim=1)
        return predicted

    def postprocess(self, data):
        response = {
                "data": int(data[0])
                }
        json_response = json.dumps(response)
        return [json_response]

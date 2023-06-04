from datasets import load_dataset
from txtai.pipeline import HFTrainer


ds = load_dataset("squad_v2")

trainer = HFTrainer()

trainer("google/bert_uncased_L-2_H-128_A-2", ds["train"].select(range(3000)), task="question-answering", output_dir="bert-qa-squadv2")


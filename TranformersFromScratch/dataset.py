from datasets import load_dataset

def load_cnn_dailymail():
    cnndm = load_dataset("cnn_dailymail", "3.0.0")
    return cnndm

def load_wikitext():
    wikitext = load_dataset("wikitext", "wikitext-103-v1")
    return wikitext


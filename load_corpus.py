from flair.data import Corpus
from flair.datasets import ColumnCorpus

def load_conll():
    # define columns
    columns = {0: 'text', 1: 'temp1', 2: 'temp2', 3: 'ner'}

    # this is the folder in which train, test and dev files reside
    data_folder = 'C:\\Users\\v-qishao\\Desktop\\flair_conll_ner\\data'

    # init a corpus using column format, data folder and the names of the train, dev and test files
    corpus: Corpus = ColumnCorpus(data_folder, columns,
                                  train_file='train.txt',
                                  test_file='test.txt',
                                  dev_file='dev.txt')
    print("train dataset:")
    print(len(corpus.train))

    print("dev dataset:")
    print(len(corpus.dev))

    print("test dataset:")
    print(len(corpus.test))
    
    return corpus

if __name__ == '__main__':
    load_conll()

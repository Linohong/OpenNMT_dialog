import sys
import numpy as np

sys.path.append('/home/nlpgpu3/LinoHong/LinoHong/Mem2Seq/')
sys.path.append('/home/nlpgpu3/LinoHong/LinoHong/Mem2Seq/utils')

def lexical_diversity(texts):
    cnt = 0
    score = 0.0
    for text in texts:
        try:
            score += len(set(text)) / len(text)
            cnt += 1
        except ZeroDivisionError:
            continue

    return float(score) / float(cnt)

if __name__ == "__main__":
    nmt_filename = './tgt-test.txt'
    m2s_filename = './dialog-babi-task1tst.txt'
    nmt = open(nmt_filename).read().strip().split('\n')  # list of sentences
    m2s = open(m2s_filename).read().strip().split('\n')  # list of sentences

    f = open('same_test.txt', 'w')
    for sent in nmt:
        for m2s_sent in m2s:
            if sent in m2s_sent:
                f.write(sent)
                f.write('\n')
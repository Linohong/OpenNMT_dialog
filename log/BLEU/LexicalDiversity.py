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
    inf_filename = './BLEU.hyp.txt'
    inference = open(inf_filename).read().strip().split('\n')  # list of sentences

    lexical_diversity_score = lexical_diversity(inference)
    print(lexical_diversity_score)
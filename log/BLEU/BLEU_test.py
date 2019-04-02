import sys
import numpy as np

sys.path.append('/home/nlpgpu3/LinoHong/LinoHong/Mem2Seq/')
sys.path.append('/home/nlpgpu3/LinoHong/LinoHong/Mem2Seq/utils')
from utils.measures import moses_multi_bleu


if __name__ == "__main__":
    inf_filename = '../baseline_pred.txt'
    ref_filename = '../../data/tgt-test.txt'
    # inf_filename = '../../../../LinoHong/Mem2Seq/BLEU.hyp.txt'
    # ref_filename = '../../../../LinoHong/Mem2Seq/BLEU.ref.txt'

    inference = open(inf_filename).read().strip().split('\n')  # list of sentences
    reference = open(ref_filename).read().strip().split('\n')  # list of sentences

    # bleu_score = moses_multi_bleu(np.array(inference), np.array(reference), lowercase=True)
    bleu_score = moses_multi_bleu(np.array(inference), np.array(reference), lowercase=True)
    print(str(bleu_score))
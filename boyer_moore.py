from readfile import read_reference_file, pattern_generator
from z_algo import get_z, naive_impl
from tqdm import tqdm
import numpy as np
def alphabet():
    return [chr(i) for i in range(65, 91)]
def get_bad_char_table(p):
    N = alphabet()
    table = np.empty(shape=(len(p), len(N)))
    table[0,:] = None
    for i in range(1, len(p)):
        n_index = ord(p[i - 1]) - ord('A')
        table[i, :] = table[i-1, :]
        table[i, n_index] = i - 1
    return table

def bad_char(p, t, table, j, k):
    x = t[j+k]
    # print(j+k)
    # return
    left_index = table[k, ord(x)-ord('A')]
    # print(left_index)
    if not np.isnan(left_index):
        return int(k-left_index)
    else:
        return 1
def get_goodsuffix_matchedpf(p):
    gs = [0]*(len(p)+1)
    z_suffix, matched_prefix = get_zsuffix_matchedprefix(p)
    for i in range(1, len(p)-1):
        j = len(p)-z_suffix[i]
        gs[j] = i
    return gs, matched_prefix
def good_suffix(p, t, j, gs, mpf, k):
    jump_length = 0
    if k >= 0:
        if gs[k+1] > 0:
            jump_length = len(p)-1-gs[k+1]
            # check_jumplen(jump_length, p, k)
        elif k == len(p) -1:
            return 1
        elif gs[k+1]==0:
            jump_length = len(p)-mpf[k+1]
            # check_jumplen(jump_length, p, k)
            # print(mpf[k+1])

    else:
        jump_length = len(p) - mpf[1]

        # print(mpf[1])


    return jump_length
def check_jumplen(jump_len, p, k):
    y = p[k]
    matched_p = p[k+1:]
    shifted_matchp = p[-jump_len-len(matched_p)+1:-jump_len+1]
    if matched_p != shifted_matchp:
        print(matched_p, shifted_matchp, k, jump_len, p)
    # print(matched_p==shifted_matchp)
def rtl_scan(p, t, j):
    k = len(p) - 1
    while k >= 0:
        if t[j+k] != p[k]:
            break
        k -=1
    return k
def boyer_moore(p, t):
    match = []
    badchar_table = get_bad_char_table(p)
    goodsuffix, matched_prefix = get_goodsuffix_matchedpf(p)
    j = 0
    while j <= len(t)-len(p):
        k = rtl_scan(p, t, j)
        if k == -1:
            match.append(j)
            jump_length = max(1, good_suffix(p, t, j, goodsuffix, matched_prefix, k))
        else:
            bc = bad_char(p, t, badchar_table, j, k)
            gs = good_suffix(p, t, j, goodsuffix, matched_prefix, k)
            jump_length = max(bc, gs)
        j += jump_length
        # print(bc,gs)
    return match

def get_zsuffix_matchedprefix(s):
    zsuffix =  get_z(s[::-1])[::-1]
    mpf = get_z(s)
    a = 0
    for i in range(len(mpf)-1, -1, -1):
        if mpf[i]==len(s)-i:
            a = max(a, mpf[i])
        mpf[i] = a
    # print(mpf, s)
    return zsuffix, mpf

def check_badchar(pattern_gen = pattern_generator('pattern-collection_2.txt'), text=read_reference_file()):
    # p = next(pattern_gen)
    t = text
    for p in pattern_gen:
        bc_match = []
        badchar_table = get_bad_char_table(p)
        n_match = naive_impl(p, t)
        j = 0
        while j <=len(t) - len(p):
            k = rtl_scan(p, t, j)
            if k == -1:
                bc_match.append(j)
                bc = 1
            else:
                bc = bad_char(p, t, badchar_table, j, k)
            # print(bc)
            j += bc
            # print(bc)
        print(len(n_match), len(bc_match), len(n_match)==len(bc_match))
def check_goodsuffix(pattern_gen = pattern_generator('pattern-collection.txt'), text=read_reference_file()):
    t = text
    for p in pattern_gen:
        gs_match = []
        n_match = naive_impl(p, t)
        goodsuffix, matched_prefix = get_goodsuffix_matchedpf(p)
        j = 0

        while j <= len(t)-len(p):

            k = rtl_scan(p, t, j)
            if k == -1:
                gs_match.append(j)
            jump_length = good_suffix(p, t, j, goodsuffix, matched_prefix, k)
            j += jump_length
        assert gs_match==n_match

def check_bm(pattern_gen = pattern_generator('pattern-collection_2.txt'), text=read_reference_file()):
    t = text
    for p in pattern_gen:
        n_match = naive_impl(p, t)
        bm_match = boyer_moore(p, t)
        assert bm_match==n_match



if __name__ == "__main__":
    # pattern_path = 'pattern-collection_2.txt'
    # text = read_reference_file()
    # pattern_gen = pattern_generator(pattern_path)
    # pattern = next(pattern_gen)
    # bm_match = boyer_moore(pattern, text)
    # n_match = naive_impl(pattern, text)
    # print(bm_match)
    # print(n_match)
    check_bm()

    # check_badchar()
    # check_goodsuffix()


from z_algo import get_z, naive_impl
from readfile import read_reference_file, pattern_generator
def get_sp(s):
    sp = [0]*len(s)
    z_list = get_z(s)
    for i in range(len(s)-1,-1,-1):
        j = i + z_list[i] - 1
        sp[j] = z_list[i]
    return sp
def kmp(p, t):
    match = []
    sp_list = get_sp(p)
    j = 0
    while j <= len(t) - len(p):

        i = 0
        while i < len(p):
            if p[i] != t[i+j]:
                break
            i += 1
        if i == len(p):
            match.append(j)
            jump_length = len(p) - sp_list[-1]
        else:
            jump_length = i-1 - sp_list[i-1]
        j += jump_length
    return match

def check(text, pattern_gen):
    for i,pattern in enumerate(pattern_gen):
        kmp_result = kmp(pattern, text)
        n_result = naive_impl(pattern, text)
        if len(kmp_result) != len(n_result):
            print(len(kmp_result),len(n_result),i, pattern)
if __name__ == '__main__':

    pattern_path = 'pattern-collection.txt'

    pattern_gen = pattern_generator(pattern_path)
    text = read_reference_file()
    check(text, pattern_gen)


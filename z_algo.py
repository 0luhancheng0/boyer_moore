from readfile import read_reference_file, pattern_generator
def get_z(s):
    Z_list = [0] * len(s)
    r = 0
    l = 0
    for k in range(1, len(s)):
        if k > r:
            z = 0
            for i in range(k, len(s)):
                if s[i] != s[i-k]:
                    break
                z+=1
            l = k
            r = l + z - 1
            Z_list[k] = z
        else:
            p = k - l
            if Z_list[p] < r-k+1:
                Z_list[k] = Z_list[p]
            else:
                z = 0
                for i in range(r+1, len(s)):
                    if s[i] != s[i-k]:
                        break
                    z += 1
                z += r - k + 1
                l = k
                r = l + z - 1
                Z_list[k] = z
    return Z_list


def naive_impl(pat, txt):
    result = []
    i = 0
    while i + len(pat) - 1 < len(txt):
        if txt[i:i+len(pat)] == pat:
            result.append(i)
        i+=1
    return result
def check(text, pattern_gen):
    for i,pattern in enumerate(pattern_gen):
        zlist = get_z(pattern+'$'+text)
        z_result = [i for i in zlist if i==len(pattern)]
        n_result = naive_impl(pattern, text)
        if len(z_result) != len(n_result):
            print(len(z_result),len(n_result),i, pattern)
            break
    print('all correct')
if __name__ == "__main__":

    pattern_path = 'pattern-collection.txt'
    pattern_gen = pattern_generator(pattern_path)
    text = read_reference_file()
    check(text, pattern_gen)

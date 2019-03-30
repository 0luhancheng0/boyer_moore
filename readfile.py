
def read_reference_file():
    reference_file_path = './Prac03_Supporting_Material-20190314/reference.txt'
    with open(reference_file_path, 'r') as fobject:
        return fobject.read().rstrip()
def pattern_generator(filename):

    with open("./Prac03_Supporting_Material-20190314/"+filename, 'r') as fobject:
        for i in fobject:
            yield i.rstrip()

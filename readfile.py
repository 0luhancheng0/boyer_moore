
def read_reference_file():
    with open('/Users/ChengLuhan/Desktop/FIT3155 adv data struct & algorithm/prac/prac3/Prac03_Supporting_Material-20190314/reference.txt', 'r') as fobject:
        return fobject.read().rstrip()
def pattern_generator(filename):
    with open("/Users/ChengLuhan/Desktop/FIT3155 adv data struct & algorithm/prac/prac3/Prac03_Supporting_Material-20190314/"+filename, 'r') as fobject:
        for i in fobject:
            yield i.rstrip()
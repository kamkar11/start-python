__author__ = 'student'

def histogram(s):
    dic = dict()
    for i in s:
        dic[i] = s.count(i)
    return dic

print(histogram("Ala ma kota"))


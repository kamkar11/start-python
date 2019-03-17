def histogram(text):
    dictonary = {}
    text = text.replace(" ", "")
    print(type(text))
    for element in text:
        dictonary[element] = text.count(element)
        # if (element in dictonary):
        #     dictonary[element] += 1
        # else:
        #     dictonary[element] = 1
    print(dictonary)


text = "Ala ma kota"
histogram(text)
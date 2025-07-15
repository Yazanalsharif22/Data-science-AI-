def removeSpaces(string):

    string = string.replace(" ", "")
    string = string.replace("\n", "")
    string = string[::-1]

    yield string


# a = """
# ا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط
# ظ ع غ ف ق ك ل م ن ه و ي

# """
# string_without_spacses = removeSpaces(a)
# print(string_without_spacses)

import re


x= "11111111111111111111e222"
search = re.findall("[0-9]+",x)
print(search)


x= "1111+a"
search= re.findall("[0-9.]\+",x)


x= "11111111111111111111e222"
search = re.findall("[0-9.]+(e)",x)



x= "11111111111111111111e222"
search = re.findall("^[0-9.]+e",x)


x= "11111111111111111111e222"
search = re.findall("$[0-9.]+e",x)


def match_add(string):
    if re.search('Add: \d \+ \d\d\D', string):
        return string
    else:
        return "This string does not match."

print(match_add('Add: 1 + 23'))
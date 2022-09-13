
from cgi import print_directory


with open(file="province_",encoding="utf-8") as fp:
    strs = fp.read()
    res = strs.split()
    vals = ""
    inner_cal = 0
    for val in res:
        vals += val
        inner_cal = inner_cal + 1
        if inner_cal%2 == 0:
            print(vals)
            vals = ""
        else:
            pass

    
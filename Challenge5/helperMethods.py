# helper stuff

def add_pair(item, dict):
    if (item in dict):
        dict[item] += 1
    else:
        dict[item] = 1
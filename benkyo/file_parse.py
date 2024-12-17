import os

#TODO seperate this into sorter vs incl functions
def file_parse_incl(path,incl):
    dir_list = os.listdir(path)
    #remove elements that dont match incl entry
    for i in dir_list:
        if incl not in i:
            dir_list.remove(i)

    #sort list
    dir_list.sort(key=lambda x: int((x.split("-")[1]).split(".")[0]))
    return dir_list
    #print(dir_list)



import os

def sub_edit(filename,target_word,changer):
    with open(filename,"r") as file:
        text = file.read().split("\n")
        for line in text:
            if target_word in line.lower():
                line.lower().replace(target_word,changer)
    with open(filename,"w") as file:
        file.write("\n".join(line))
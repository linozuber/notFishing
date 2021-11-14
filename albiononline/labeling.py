import os

def labelNegative():
    with open("neg.txt", "w") as f:
        for filename in os.listdir("img/neg_down"):
            f.write("img/neg_down/" + filename + "\n")

labelNegative()

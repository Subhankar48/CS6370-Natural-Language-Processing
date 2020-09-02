import numpy as np

def edit_distance(str1, str2):
    t = np.zeros((len(str1)+1, len(str2)+1))
    t[0,:] = np.arange(len(str2)+1)
    t[:,0] = np.arange(len(str1)+1)
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                t[i+1, j+1]  = t[i,j]
            else:
                t[i+1, j+1] = 1 + min(t[i,j], t[i+1,j], t[i,j+1])
    return t[-1,-1]

if __name__=="__main__":
    w1 = input("Enter the first word.\n")
    w2 = input("Enter the second word.\n")
    print(f"The edit distance between {w1} and {w2} is {edit_distance(w1,w2)}")
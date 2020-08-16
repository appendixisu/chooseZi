# !/usr/bin/python
# coding:utf-8

def read4808():
    f = open('/Users/wei-chilan/Documents/python/ziWebCrawler/4808.txt')

    text = []
    for line in f:
        text.append(line)

    word = []
    for j in range(len(text)):
        if (j%2 == 1):
            at = text[j].split(' ')
            for i in range(len(at)):
                if (i%2 == 1):
                    word.append(at[i])
                else:
                    continue
        else :
            continue
    return word

if __name__ == "__main__":
    abcd = input()
    www = read4808()
    # del(www[0:105])
    for i in range(len(www)):
        if (www[i] == abcd):
        # if(i < 5):
            print(i,":",www[i])
            print('剩下:',4808-i)
            s = (4808-i)*0.5*40
            print('預估還要:', s, '秒=', s/60, '分=', s/3600, '時')

    # print(len(read4808()))

    # print('\',\''.join(word))
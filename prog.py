import pandas as pd

def one():
    print('one')

    textfile = open('text.txt','r',encoding='utf8')
    text = textfile.read()
    print(text)
    textfile.close()

    array = pd.read_csv('letters.csv', delimiter=';')
    farray = array.sort_values(by=['frequ'], ascending=False)
    farray = farray.reset_index(drop=True)

    textarray=pd.read_csv('fortext.csv', delimiter=';')

    # считаем
    for j in range(0,len(text)):
        for i in range (0,33):
            if text[j] == textarray.letter[i]:
                textarray.loc[i, 'frequ'] += 1

    finaltextarray = textarray.sort_values(by=['frequ'], ascending=False)
    finaltextarray = finaltextarray.reset_index(drop = True)

    newtext=text

    # заменяем
    for j in range(0,len(text)):
        for i in range(0,33):
            if text[j]==finaltextarray.letter[i]:
                newtext=newtext[:j] + farray.letter[i]+newtext[j+1:]

    print(newtext)


def two():
    print('two')

    textfile = open('text.txt','r',encoding='utf8')
    text = textfile.read()
    print(text)
    textfile.close()

    array = pd.read_csv('bigrams.csv', delimiter=';')
    farray = array.sort_values(by=['frequ'], ascending=False)
    farray = farray.reset_index(drop=True)

    textarray = pd.read_csv('fortextb.csv', delimiter=';')

    # считаем
    for j in range(0,len(text)-1):
        for i in range (0,961):
            if (text[j] == textarray.letter1[i])&(text[j+1] == textarray.letter2[i]):
                textarray.loc[i, 'frequ'] += 1

    finaltextarray = textarray.sort_values(by=['frequ'], ascending=False)
    finaltextarray = finaltextarray.reset_index(drop=True)

    newtext = text

    newtextl = list(newtext)
    newtextdf = pd.DataFrame(newtextl, columns=['letter'])
    newtextdf['chflag'] = 0

    # заменяем
    for j in range(0, len(newtextdf) - 1):
        for i in range(0, len(farray)):
            if (newtextdf.letter[j] == finaltextarray.letter1[i]) and (newtextdf.letter[j + 1] == finaltextarray.letter2[i]) and ((newtextdf.chflag[j] == 0) and (newtextdf.chflag[j+1] == 0)):
                newtextdf.loc[j, 'letter'] = farray.letter1[i]
                newtextdf.loc[j, 'chflag'] = 1
                newtextdf.loc[j + 1, 'letter'] = farray.letter2[i]
                newtextdf.loc[j + 1, 'chflag'] = 1

    newtextl = newtextdf['letter'].values.tolist()
    newtext = ''.join(newtextl)
    print(newtext)


if __name__ == "__main__":  # основная функция
    print('\n')
    one()
    print('\n')
    two()
    print('\n')
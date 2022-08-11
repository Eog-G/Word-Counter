import os
import pandas as pd
import plotly.express as px

path = r"\HP"
BOOKS = os.listdir(path)
for i,b in enumerate(BOOKS):
    BOOKS[i] = path + r'\\' + BOOKS[i]

def remove_punc(x):
    x = x.lower()
    x = x.replace('”', " ")
    x = x.replace('“', " ")
    x = x.replace(r'\n', ' ')
    x = x.replace(',', ' ')
    x = x.replace('.', ' ')
    x = x.replace('?', ' ')
    x = x.replace('!', ' ')
    x = x.replace('—', ' ')
    x = x.replace("'", ' ')
    x = x.replace(']', ' ')
    x = x.replace('[', ' ')
    x = x.replace(';', ' ')
    x = x.replace("’s", ' ')
    
    if(x[0:6] == 'page |'):
        return ''

    return x

words = []


for i,o in enumerate(BOOKS):
    with open(BOOKS[i], encoding="utf8") as book:
        lines = book.readlines()

        for x in lines: # x = index with 1 string
            string = str(x)
            string = remove_punc(string)
            a = string.split()
            for z in a:
                words.append(z)

    

words = sorted(words)

d_words = {}

for x in words:
    if x in d_words:
        d_words[x] += 1
    else:
        d_words[x] = 1

d_words = dict(sorted(d_words.items(), key=lambda item: item[1]))

# Count specific word
try:
    print(d_words['train'])
except KeyError:
    print("Word not found.")

l_words = [(k, v) for k, v in d_words.items()]

for i in range(0,len(l_words) - 50):
    l_words.pop(0)

df = pd.DataFrame(l_words, columns=['Word', 'Occurences'])

fig = px.bar(df, x='Word', y='Occurences', color="Occurences", title="Most common words")
fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
fig.update_layout(legend=dict(
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'))
fig.show()

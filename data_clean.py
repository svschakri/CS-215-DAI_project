import pandas as pd

df  = pd.read_csv("student_lifestyle_dataset.csv")

pd.options.display.max_rows = 100
cols = list(df)
print(cols)
df[cols[-1]] = df[cols[-1]].replace("Low" , 0)
df[cols[-1]] = df[cols[-1]].replace("Moderate" , 1)
df[cols[-1]] = df[cols[-1]].replace("High" , 2)

df[cols[1:-1]] = df[cols[1:-1]].map('{:.2f}'.format)
df[cols[0]] = df[cols[0]].astype(int)

for i in range(len(cols)) :
    max_len = df[cols[i]].astype(str).str.len().max()
    df[cols[i]] = df[cols[i]].astype(str).str.zfill(max_len)

df.to_csv("student_lifestyle_dataset.csv",index=False)

print(df) 
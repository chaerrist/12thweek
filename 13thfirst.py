from faker import Faker as fk
import pandas as pd 
import os


folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)

# print(df.name == "김민석")
# print(df.company == "김이심")

# tmp = df[df.postcode > 70000]
# print(tmp)

# res = df[df.color == "Olive"].head(1)
# print(res)

# res = df[df.postcode > 70000][["name", "postcode", "color"]]
# print(res)
# print(res.count())

# temp = df.postcode.mean()
# temp = df.postcode.sum()
# print(temp)

# temp = df[df.color=="Green"].postcode.mean()
# print(temp)

# temp = df[df.color=="Green"].postcode.sum()
# print(temp)

# tmp = df[df.postcode > df.postcode.mean()][["name", "postcode"]]
# tmp = df[df.postcode > df.postcode.mean()]
# print(tmp)

# temp = df.company.isnull()
# # temp = df.name.empty
# print(temp)

# temp = df[df.company.isnull()][["name", "postcode"]]
# print(temp)

# temp = df.company.isnull()

# for el in temp :
#     if el == True :
#         print(el)

# temp = df[(df.color == "Green")]
# temp = df[~(df.color == "Green")]
# temp = df[~(df.color == "Green")][["name"]]
# print(temp)
# print(temp.count())

# temp = df[(df.color == "Green") & (df.postcode > 70000)]
# temp = df[(df.color == "Green") | (df.postcode > 70000)]
# temp = df[(df.color == "Green") | (df.postcode > 70000)][["name"]]
# print(temp)

# temp = df.sort_values("postcode")
# temp = df.sort_values("postcode", ascending= False)
# temp = df.sort_values("name", ascending= True)
# print(temp)

col = ['Machine','Country','Price','Brand']
data = [['TV','Korea',1000,'A'],
        ['TV','Japan',1300,'B'],
        ['TV','China',300,'C'],
        ['PC','Korea',2000,'A'],
        ['PC','Japan',3000,'E'],
        ['PC','China',450,'F']]

df = pd.DataFrame(data=data, columns=col)

print(df)
print("\n-------------------\n")
# print(df.pivot(index='Machine',columns='Country',values='Price'))
# print(df.pivot(index='Brand',columns='Country',values='Price'))
print(df.pivot(index='Country',columns='Machine',values='Price'))
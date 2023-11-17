import pandas as pd

# df = pd.DataFrame([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]])

# print(df)
# print(df[1])
# print(df[1][1])

# dt = {
#     "x" : [10, 15, 20],
#     "y" : [50, 55, 60],
#     "z" : [100, 110, 120]
# }

# idx = ["x축", "y축", "z축"]

# fr = pd.DataFrame(data=dt, index=idx)

# # print(fr)
# # print("\n-------------------\n")
# # print(fr["x"])
# # print("\n-------------------\n")
# # print(fr.x)
# # print("\n-------------------\n")
# # print(fr.iloc[2])
# # print("\n-------------------\n")
# # print(fr.loc["y축"])


# frs = pd.DataFrame(fr,columns=["x", "y", "z", "t"])
# print(frs)
# print("\n-------------------\n")

# frs["t"] = [60, 120, 180]
# print(frs)
# print("\n-------------------\n")

# # frs.loc["t축"] = [100, 200, 300, 400]
# # print(frs)
# # print("\n-------------------\n")

# # frs.loc["t축"] = [500, 600, 700, 800]
# # print(frs)
# # print("\n-------------------\n")

# #행 삭제
# frs.drop("x", axis=1, inplace=True)
# print(frs)
# print("\n-------------------\n")

# # 열 삭제
# frs.drop("x축", inplace=True)
# print(frs)
# print("\n-------------------\n")


# dt = [[1,10,100],[2,20,200],[3,30,300]]
# col = ["x","y","z"]
# idx = ["x축","y축","z축"]

# df = pd.DataFrame(data=dt,index=idx,columns=col)

# print(df)
# print("\n-------------------\n")

# # print(df["x"])
# # print("\n-------------------\n")

# # print(df.loc["x축"])
# print("\n-------------------\n")

# print(df + 1)
# print("\n-------------------\n")

# print(df.div(100))
# print("\n-------------------\n")

# print(df / 100)
# print("\n-------------------\n")

# print(df.mul(100))
# print("\n-------------------\n")

# print(df * 100)
# print("\n-------------------\n")



# # 같은 인덱스끼리 연산
# dt2  = [[0],[2],[3]]
# df2 = pd.DataFrame(data=dt2,index=["x축","y축","z축"],columns=["y"])
# print(df2)
# print("\n-------------------\n")

# # print(df.div(df2))
# # print("\n-------------------\n")

# print(df.div(df2, fill_value=1))
# print("\n-------------------\n")

# dt = [[1,10,100],[2,20,200],[3,30,300]]
# col = ["col1","col2","col3"]
# idx = ["한화","키움","기아"]

# df = pd.DataFrame(data=dt,index=idx,columns=col)

# print(df)
# print("\n-------------------\n")

# print(df + 1)
# print("\n-------------------\n")

# # print(df.loc["한화"])
# # print("\n-------------------\n")

# # 같은 인덱스끼리 연산
# dt2  = [[0],[2],[3]]
# df2 = pd.DataFrame(data=dt2,index=["한화","키움","기아"],columns=["y"])
# print(df2)
# print("\n-------------------\n")

# print(df.mul(df2))
# print("\n-------------------\n")

# print(df.div(df2, fill_value=100))
# print("\n-------------------\n")

# idx = [('row1', 'val1'), ('row1', 'val2'), ('row2', 'val1'), ('row2', 'val2'), ('row2', 'val3'), ('row3', 'val2'),('row3', 'val3')]
# dt = [ [1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21]]

# ind = pd.MultiIndex.from_tuples(idx)
# df = pd.DataFrame(dt, columns=['col1', 'col2', 'col3'], index = ind)

# print(df)
# print("\n-------------------\n")

# print(df.loc["row1"])
# print("\n-------------------\n")

# print(df.loc[("row2", "val3")])
# print("\n-------------------\n")

# print(df.iloc[0])
# print("\n-------------------\n")

# print(df.loc[("row3", "val3"), "col1"])
# print("\n-------------------\n")


import numpy as np

dt = np.random.randint(10, size=(5, 5))
df = pd.DataFrame(dt)

print(df)
print("\n-------------------\n")

print(df[2])
print("\n-------------------\n")

print(df.loc[2])
print("\n-------------------\n")

print(df.loc[3][1])
print("\n-------------------\n")

print(df.head(2))
print("\n-------------------\n")

print(df.tail(3))
print("\n-------------------\n")

print(df.sample())
print("\n-------------------\n")

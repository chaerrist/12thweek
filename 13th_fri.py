import pandas as pd
import os

folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)

# df["aver"] = df.postcode.rank(method="average")
# print(df[["postcode", "aver"]])

# df["first"] = df.postcode.rank(method="first")
# print(df[["postcode", "first"]])

# df["dense"] = df.postcode.rank(method="dense")
# print(df[["postcode", "dense"]])

# df["min"] = df.postcode.rank(method="min")
# print(df[["postcode", "min"]])

# df["max"] = df.postcode.rank(method="max")
# df["max"] = df.postcode.rank(method="max", ascending= False)
# print(df[["postcode", "max"]])

# print(df[["postcode", "first", "dense", "min", "max", "aver"]])

# print(df.transpose())

# print(df["postcode"].expanding().sum())
# print(df["postcode"].expanding())

# print(df.postcode.idxmax(axis=0))
# print(df.postcode.idxmin(axis=0))

# print(df.empty)
# print(df.postcode.empty)

# print(df.isin(["이정희"]))
# print(df.isin([17238]))
# print(df.isin([32792, "이정희"]))
# print(df.isin([17238, 32792, "이정희"]))

# period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
# dt = {"col1":[1,2,3,4,5,6],"col2":period}
# idx = ["row1","row2","row3","row4","row5","row6"]

# pf = pd.DataFrame(data=dt, index=idx)
# print(pf)

# i = pd.date_range("2023-11-10", periods=10, freq="1H")
# # i = pd.date_range("2023-11-10", periods=10, freq="3H")
# dtf = pd.DataFrame({"col1":[1,2,3,4,5,6,7,8,9,10]}, index=i)
# print(dtf)
# print("\n------------------\n")

# print(dtf.at_time("09:00"))
# print(dtf.at_time("03:00"))
# print(dtf.between_time(start_time="12:00", end_time="00:00"))

# i = pd.date_range("2023-11-10", periods=10, freq="3D")
# dtf = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10]}, index=i)
# print(dtf)

# print(dtf.first("3D"))
# print(dtf.last("7D"))

import FinanceDataReader as fdr

ksp = fdr.DataReader("KS11", "2001")
# print(ksp)
# print(ksp["High"].max())
# print(ksp["High"].idxmax())
# print(ksp["Low"].min())
# print(ksp["Low"].idxmin())

# res = ksp["Volume"].nlargest(n=5)
# print(res)

# res = ksp["Volume"].nsmallest(n=5)
# print(res)

# res = ksp["Close"].nsmallest(n=5)
# print(res)

# cond = ksp["Close"] >= 3000
# res = ksp[cond].index[0]
# print(res)

# ksp["up"] = ksp["Volume"] > ksp["Volume"].shift()
# print(ksp)

# ksp["grp"] = ksp["up"] != ksp["up"].shift().cumsum()
# print(ksp)

# ksp["up_cnt"] = ksp["grp"].groupby(ksp["grp"].values).cumcount() + 1
# print(ksp)

# print(ksp["up_cnt"].max())

##공공데이터 

# target = "./data/apt.csv"

# df = pd.read_csv(target, encoding="CP949")
# df.to_csv("./data/conv_apt.csv", encoding="utf8")

# print(df.head())

df = pd.read_csv("./data/conv_apt.csv", index_col = 0)
print(df.head())

df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
# print(df)
# print(df.dtypes)

df["분양가"] = df["분양가"].convert_dtypes()
# print(df.dtypes)

arr = df.to_numpy()
# print(arr)
# print(arr[2])
# print(len(arr))

print(df.describe())
print(df.transpose())
print(df.T.head())
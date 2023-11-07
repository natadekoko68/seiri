import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from scipy.stats import linregress
import pprint

# data_path = "/Users/kotaro/Desktop/生理データ/アイソトープ/生理アイソトープ.csv"
data_path = "/Users/kotaro/Desktop/生理データ/アイソトープ/Book5.csv"
# data_path = "/Users/kotaro/Desktop/生理データ/アイソトープ/アイソトープ2022データ.csv"

df = pd.read_csv(data_path)



df = df.drop(["Unnamed: 0","Area","Min","Max"],axis=1)
print(df)

content_labels = [
    "count_sum",
    "count_sum",
    "blank",
    "blank",
    "zero",
    "zero",
    "standard1",
    "standard1",
    "standard2",
    "standard2",
    "standard3",
    "standard3",
    "standard4",
    "standard4",
    "standard5",
    "standard5",
    "standard6",
    "standard6",
    "standard7",
    "standard7",
    "standard8",
    "standard8",
    "sample1",
    "sample1",
    "sample2",
    "sample2",
    "sample3",
    "sample3",
    "sample4",
    "sample4",
    "sample5",
    "sample5",
    "sample6",
    "sample6",
    "sample7",
    "sample7",
]
df["label"] = content_labels

count_sum = df.loc[df["label"] == "count_sum","Mean"].mean()
blank = df.loc[df["label"] == "blank","Mean"].mean()
# print(count_sum,blank)

df.loc[df["label"].str.contains("standard"), "b_t"] = (df.loc[df["label"].str.contains("standard"), "Mean"] - blank) / (count_sum - blank) * 100
df.loc[df["label"].str.contains("sample"), "b_t"] = (df.loc[df["label"].str.contains("sample"), "Mean"] - blank) / (count_sum - blank) * 100

df.index = np.arange(1, len(df)+1)
# print(df)

df_kenryosen = df[df["label"].str.contains("standard")]

kenryosen_concentrations = [80/(2**(7-i)) for i in range(8)]
# print(kenryosen_concentrations)
kenryosen_values = []
for i in df_kenryosen["label"].unique():
    kenryosen_values.append(df_kenryosen[df_kenryosen["label"]==i]["b_t"].mean())
    # print(i)
# print(kenryosen_values)

kenryosen_concentrations_log = np.log(np.array(kenryosen_concentrations))
slope, intercept, r_value, p_value, std_err = linregress(kenryosen_concentrations_log, kenryosen_values)
print(slope, intercept, r_value, p_value, std_err)
lin_space = np.linspace(10**(-5),1000,100)
plt.plot(lin_space,np.log(lin_space) * slope + intercept,color="red")
plt.scatter(kenryosen_concentrations,kenryosen_values)
plt.xscale("log")
plt.xlim([5*10**(-1),100])
plt.ylim([0,max(kenryosen_values)*1.2])
plt.text(13,20,"y = " + str(round(slope,3)) + " log(x) " + " + " + str(round(intercept,3)) + " \n ( R$^{2}$ = "+ str(round(r_value**2,3)) + " )")
plt.xlabel("cAMP濃度 (pmol/mL)")
plt.ylabel("B/T ($\%$)")
plt.grid()
plt.title("cAMP濃度とB/T($\%$)の関係")
plt.tight_layout()
if "2022" in data_path:
    plt.savefig("/Users/kotaro/Desktop/アイソトープ検量線2022.jpg", dpi=300)
else:
    plt.savefig("/Users/kotaro/Desktop/アイソトープ検量線2023.jpg",dpi=300)
plt.show()





df.loc[df["label"].str.contains("sample"),"cAMP_concentrations"] = np.e ** ((df.loc[df["label"].str.contains("sample"),"b_t"] - intercept) / slope)

# print(df)

df_samples = df[df["label"].str.contains("sample")]
# print(df_samples)
cAMP = {}
cAMP_display = []
sum = 0
for i in df_samples["label"].unique():
    cAMP_display.append(df_samples[df_samples["label"] == i]["cAMP_concentrations"].mean())
    cAMP[i] = df_samples[df_samples["label"] == i]["cAMP_concentrations"].mean()
    sum += df_samples[df_samples["label"] == i]["cAMP_concentrations"].mean()
# pprint.pprint(cAMP)


plt.bar([i for i in range(len(cAMP_display))], cAMP_display)
# plt.xticks([i for i in range(len(cAMP_display))], ["No." + str(2*i+1) + ","+ str(2*i+2) for i in range(len(cAMP_display))])
plt.xticks([i for i in range(len(cAMP_display))], ["PBS","CT:0.2","CT:2","CT:20","CT:200","(CT:2)*5","(CT:200)*10"])

plt.xlabel("サンプル番号")
plt.ylabel("cAMP濃度 (pmol/mL)")
plt.title("各サンプルのcAMP濃度")
plt.tight_layout()
if "2022" in data_path:
    plt.savefig("/Users/kotaro/Desktop/cAMP濃度2022.jpg", dpi=300)
else:
    plt.savefig("/Users/kotaro/Desktop/cAMP濃度2023.jpg",dpi=300)
plt.show()
#
standardized_cAMP = {}
for key in cAMP:
    standardized_cAMP[key] = round(cAMP[key]/sum*100,4)
# pprint.pprint(standardized_cAMP)



# from tabulate import tabulate
# df = pd.read_csv(data_path)
# # df = df.drop(["Unnamed: 0"],axis=1)
# df = df.rename(columns={"Unnamed: 0":"N0"})
# print(tabulate(df, df.columns, tablefmt='github', showindex=False))


import pytab as pt
df = pd.read_csv(data_path)
df = df.drop(["Unnamed: 0"],axis=1)
# df = df.rename(columns={"Unnamed: 0":"N0"})
rows = [i for i in range(1,37)]
pt.table(
    data=df,
    rows = rows,
    th_type='dark',
    table_type='striped',
    figsize=(5,10)
)
if "2022" in data_path:
    pt.save("/Users/kotaro/Desktop/計測値2022.jpg")
else:
    pt.save("/Users/kotaro/Desktop/計測値2023.jpg")

pt.show()
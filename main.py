import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import pandas as pd

"""0"""
no_tnf_1_raw = np.array([4542.201,4915.88,5913.914,4311.511,4007.668,5164.473,5419.644,5581.776])
no_tnf_2_raw = np.array([4910.563,4900.673,5215.944,4857.628,4877.208,6313.648,6078.414,6396.854,6530.685])
no_tnf_3_raw = np.array([4677.375,6527.758,4599.046,5928.969,4901.645,5204.097,5286.011])
no_tnf_4_raw = np.array([5042.158,4131.535,4279.886,5103.673,5615.572,5254.339,4895.331,4430.852,5521.278,5624.594])
no_tnf_5_raw = np.array([4455.874,5297.917,4181.959,4194.904,4793.028,4707.881,5653.838,5813.804,5170.854,5284.536,4749.668])

no_tnf_bg_1 = 1820.265
no_tnf_bg_2 = 2289.707
no_tnf_bg_3 = 2333.178
no_tnf_bg_4 = 2105.23
no_tnf_bg_5 = 2029.132

no_tnf_1 = no_tnf_1_raw - no_tnf_bg_1
no_tnf_2 = no_tnf_2_raw - no_tnf_bg_2
no_tnf_3 = no_tnf_3_raw - no_tnf_bg_3
no_tnf_4 = no_tnf_4_raw - no_tnf_bg_4
no_tnf_5 = no_tnf_5_raw - no_tnf_bg_5

no_tnf_all = []
for i in no_tnf_1:
    no_tnf_all.append(i)
for i in no_tnf_2:
    no_tnf_all.append(i)
for i in no_tnf_3:
    no_tnf_all.append(i)
for i in no_tnf_4:
    no_tnf_all.append(i)
for i in no_tnf_5:
    no_tnf_all.append(i)
print(len(no_tnf_all))


"""0.5"""
tnf_half_1_raw = np.array([6622.535,6178.528,6950.033,5126.108,6150.252,7518.797,6646.664,8539.671,7757.857,3273.386])
tnf_half_2_raw = np.array([5398.699,7145.066,6657.167,5733.379,6541.451,6683.17,6508.452])
tnf_half_3_raw = np.array([7282.165,7423.307,6504.794,6651.484,7828.497,7594.306])
tnf_half_4_raw = np.array([5337.65,5359.75,7318.474,6542.086,6127.423,5477.664,7039.975,5908.263,6441.952,5718.95,7660.726])
tnf_half_5_raw = np.array([5429.207,5351.403,5612.236,4730.863,5954.754,10984.62,4828.156,6162.524,5345.297])

tnf_half_bg_1 = 1859.625
tnf_half_bg_2 = 2005.23
tnf_half_bg_3 = 2272.897
tnf_half_bg_4 = 3112.002
tnf_half_bg_5 = 2398.627

tnf_half_1 = tnf_half_1_raw - tnf_half_bg_1
tnf_half_2 = tnf_half_2_raw - tnf_half_bg_2
tnf_half_3 = tnf_half_3_raw - tnf_half_bg_3
tnf_half_4 = tnf_half_4_raw - tnf_half_bg_4
tnf_half_5 = tnf_half_5_raw - tnf_half_bg_5

tnf_half_all = []
for i in tnf_half_1:
    tnf_half_all.append(i)
for i in tnf_half_2:
    tnf_half_all.append(i)
for i in tnf_half_3:
    tnf_half_all.append(i)
for i in tnf_half_4:
    tnf_half_all.append(i)
for i in tnf_half_5:
    tnf_half_all.append(i)
print(len(tnf_half_all))

"""10"""
tnf_10_1_raw = np.array([7910.745,10099.211,8612.875,8754.999,6140.461,11635.054,6985.912])
tnf_10_2_raw = np.array([6106.227,9569.013,9374.088,14920.978,6373.751,9627.45,6034.653,5534.27,6834.111,5489.461])
tnf_10_3_raw = np.array([7129.333,6316.453,8226.231,6691.987,4858.872,7651.956,4509.804,6627.454,5941.291])
tnf_10_4_raw = np.array([6403.367,7556.08,8013.578,7156.194,10016.166,9662.354,6730.641,7636.857])
tnf_10_5_raw = np.array([8723.105,8933.414,9602.669,7647.685,7956.455,8505.224])

tnf_10_bg_1 = 2299.539
tnf_10_bg_2 = 1832.03
tnf_10_bg_3 = 1911.882
tnf_10_bg_4 = 2117.987
tnf_10_bg_5 = 2383.207

tnf_10_1 = tnf_10_1_raw - tnf_10_bg_1
tnf_10_2 = tnf_10_2_raw - tnf_10_bg_2
tnf_10_3 = tnf_10_3_raw - tnf_10_bg_3
tnf_10_4 = tnf_10_4_raw - tnf_10_bg_4
tnf_10_5 = tnf_10_5_raw - tnf_10_bg_5

tnf_10_all = []
for i in tnf_10_1:
    tnf_10_all.append(i)
for i in tnf_10_2:
    tnf_10_all.append(i)
for i in tnf_10_3:
    tnf_10_all.append(i)
for i in tnf_10_4:
    tnf_10_all.append(i)
for i in tnf_10_5:
    tnf_10_all.append(i)
print(len(tnf_10_all))

"""main"""

lst_category = []
lst_value = []
for i in no_tnf_all:
    lst_category.append("0")
    lst_value.append(i)
for i in tnf_half_all:
    lst_category.append("0.5")
    lst_value.append(i)
for i in tnf_10_all:
    lst_category.append("10")
    lst_value.append(i)

df = pd.DataFrame({
    "category": lst_category,
    "value": lst_value
})

print(df)

fig = plt.figure(figsize=(6.4*1.2, 4.8*1.2))
plt.title("       TNF$\\alpha$の濃度と細胞核内のNF$\\kappa$Bの蛍光輝度の関係",fontsize=16)
sns.violinplot(data=df,x='category', y='value', inner="quartile", color="0.90")
sns.swarmplot(data=df, x='category', y='value', hue='category', palette=["green", "orange", "skyblue"])

plt.xlabel("TNF$\\alpha$の濃度(ng/mL)",fontsize=15)
plt.ylabel("細胞核内のNF$\\kappa$Bの蛍光輝度(a.u.)",fontsize=15)
plt.tight_layout()
plt.grid(visible=None, which='major', axis='y')
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
# plt.plot([0, 1], [15500, 15500], color="black")
# plt.text(0.35,15800,"p < 0.001")
# plt.plot([1, 2], [15000, 15000], color="black")
# plt.text(1.35,15300,"p < 0.001")
# plt.plot([0, 2], [16500, 16500], color="black")
# plt.text(0.85,16800,"p < 0.001")

plt.plot([0, 0.98], [15500, 15500], color="black", marker = 3)
plt.text(0.5,15200,"*",fontsize=20,horizontalalignment='center')
plt.plot([1.02, 2], [15750, 15750], color="black", marker = 3)
plt.text(1.5,15450,"*",fontsize=20,horizontalalignment='center')
plt.plot([0, 2], [16500, 16500], color="black", marker = 3)
plt.text(1.0,16200,"*",fontsize=20,horizontalalignment='center')

plt.text(1.7,-2500,"*  :  p < 0.001",fontsize=13)


plt.tick_params(bottom=False, left=False, right=False, top=False)
plt.savefig("/Users/kotaro/Desktop/TNF濃度と蛍光輝度の関係.jpg",dpi=300)
plt.show()

import scipy.stats as st
print(st.ttest_ind(no_tnf_all,tnf_half_all).pvalue)
print(st.ttest_ind(tnf_half_all,tnf_10_all).pvalue)
print(st.ttest_ind(tnf_10_all,no_tnf_all).pvalue)

"""
Based on the Original file which located at
    https://colab.research.google.com/drive/1kHfD5eP91IBF5Shguq4muPIEib9gME0Y

Authors: Ece Beren GENÇ, ...
Contributors: ...
"""
import pandas as pd
from data.insight_utils import *

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv("kdk_all_data_n10349.csv", index_col=None)

check_df(df)

# Değişken türlerinin belirlenmesi
categorical_cols, numerical_cols, cardinal_cols, nominal_cols = grab_col_names(df, categorical_threshold=5,
                                                                               cardinal_threshold=20)

print("Categorical column names: {}".format(categorical_cols))
print("Numerical column names: {}".format(numerical_cols))
print("Cardinal column names: {}".format(cardinal_cols))
print("Nominal column names: {}".format(nominal_cols))

data_info = MissingUniqueStatistics(df)
# data_info = data_info.set_index("Variable")
data_info

# target_column = "Başvuru No"
print(df.columns)
target_column = "karaR_TURU"
histogram(df, target_column)

for col in numerical_cols:
    print(col, check_outlier(df, col))

for col in numerical_cols:
    grab_outliers(df, col, True)

for col in numerical_cols:
    replace_with_thresholds(df, col)

for col in numerical_cols:
    print(col, check_outlier(df, col))

df.isnull().sum()

missing_values_table(df)

na_columns = missing_values_table(df, na_name=True)

df = quick_missing_imp(df, num_method="median", cat_length=17)

# Kategorik değişkenlerin incelenmesi

for col in categorical_cols:
    cat_summary(df, col, plot=True, savefig=False)

target = ""
for col in categorical_cols:
    target_summary_with_categorical_data(dataframe=df, target=target, categorical_col=col)

for col in numerical_cols:
    num_summary(df, col, True)

corr = df[numerical_cols].corr()

sns.set(rc={'figure.figsize': (12, 12)})
sns.heatmap(corr, cmap="RdPu")
plt.show(block=True)

high_correlated_cols(df, plot=True)

for col in numerical_cols:
    target_summary_with_numerical_data(df, target, col)

rare_analyser(df, "SalePrice", categorical_cols)

# Chi-Square test for Nominal Features
nominal_cols_for_exclude = []

for col in nominal_cols:
    chi_score, degree_f, p = chi2_by_hand(df, col, target)
    if p >= 0.05:
        nominal_cols_for_exclude.append(col)
    else:
        print(f'Chi2_score: {chi_score}, Degrees of freedom: {degree_f}, p-value: {p}')

print(nominal_cols_for_exclude)

# ANOVA Test for Numerical Features

import statsmodels.api as sm
from statsmodels.formula.api import ols

numerical_cols_for_exclude = []

for col in numerical_cols:
    model = ols(target + '~' + col, data=df).fit()  # Ordinary least square method
    result_anova = sm.stats.anova_lm(model, typ=2)  # ANOVA Test
    if result_anova.loc[col]["PR(>F)"] >= 0.05:
        numerical_cols_for_exclude.append(col)  # Save column names with pi-value greater than 0.05
    else:
        print(result_anova)
        print("\n")

print(numerical_cols_for_exclude)
df_new = df.drop(columns=nominal_cols_for_exclude)  # data set changed

# Değişken türlerin güncellenmesi
categorical_cols, numerical_cols, cardinal_cols, nominal_cols = grab_col_names(df_new, categorical_threshold=6,
                                                                               cardinal_threshold=20)


binary_cols = [col for col in df_new.columns if df_new[col].dtypes == "O" and df_new[col].nunique() == 2]
binary_cols

for col in binary_cols:
    df_new = label_encoder(df_new, col)


one_hot_encoding_cols = [col for col in categorical_cols if 10 >= df_new[col].nunique() > 2 and col != target_column]

df_new = one_hot_encoder(df_new, one_hot_encoding_cols,drop_first=True)
df_new.columns = [col.upper() for col in df_new.columns]

# Son final değişken türleri
categorical_cols, numerical_cols, cardinal_cols, nominal_cols = grab_col_names(df_new,
                                                                               categorical_threshold=5,
                                                                               cardinal_threshold=20)

categorical_cols = [col for col in categorical_cols if target_column not in col]

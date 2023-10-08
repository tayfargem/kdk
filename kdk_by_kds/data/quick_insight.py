import pandas as pd
from data.insight_utils import *

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv("kdk_all_data_n10349.csv", index_col=None)

check_df(df)

# Değişken türlerinin belirlenmesi
categorical_cols, numerical_cols, cardinal_cols, nominal_cols = grab_col_names(df, categorical_threshold=5, cardinal_threshold=20)

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

missing_values_table(df)

na_columns = missing_values_table(df, na_name=True)

# cat_summary
for col in cat_cols:
    cat_summary(df, col, plot=True, savefig=False)

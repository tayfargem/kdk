from insight_utils import *

df =""

check_df(df)

# Değişken türlerinin belirlenmesi
cat_cols, num_cols, car_cols, nom_cols = grab_col_names(df, categorical_threshold=5, cardinal_threshold=20)

print("Categorical column names: {}".format(cat_cols))
print("Numerical column names: {}".format(num_cols))
print("Cardinal column names: {}".format(car_cols))
print("Nominal column names: {}".format(nom_cols))

data_info = MissingUniqueStatistics(df)
# data_info = data_info.set_index("Variable")
data_info

target_column = "Başvuru No"

histogram(df, target_column)

missing_values_table(df)

na_columns = missing_values_table(df, na_name=True)

# cat_summary
for col in cat_cols:
    cat_summary(df, col, plot=True, savefig=False)

from import_libs import *

train_data_path = 'datasets/Fake-Instagram-Profile-Detection-main/Insta_train1.csv'
test_data_path = 'datasets/Fake-Instagram-Profile-Detection-main/Insta_test.csv'

pd.read_csv(test_data_path)
pd.read_csv(train_data_path)

# Load the training dataset
instagram_df_train=pd.read_csv(train_data_path)
instagram_df_train

# Load the testing data
instagram_df_test=pd.read_csv(test_data_path)
instagram_df_test

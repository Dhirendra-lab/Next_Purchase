import pandas as pd
import numpy as np
pd.options.display.max_colwidth = 100

def report_generation(all_files,customer_data,products_data):

    # Selecting specific column form products_data
    products_data = products_data[['product_id', 'product_category']]

    df_from_each_file = (pd.read_json(f,lines=True) for f in all_files)
    concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)

    #count of dictionary inside list
    len_of_list = concatenated_df['basket'].str.len()

    #created datafram contain product_id  & price
    product_id_price = pd.DataFrame(np.concatenate(concatenated_df['basket']).tolist(), index=np.repeat(concatenated_df.index, len_of_list))

    #joining product_id_price & concatenated_df
    concatenated_df = concatenated_df.drop('basket', axis=1).join(product_id_price).reset_index(drop=True)

    #Droping unwanted column
    concatenated_df.drop(['price'],axis=1)


    #join operation of customer_data with concatenated_df
    customer_details=customer_data.merge(concatenated_df,on='customer_id',how='left')

    #join operation of customer_details with products_data
    customer_product_details=customer_details.merge(products_data,on='product_id',how='left')

    customer_product_details=customer_product_details[['customer_id','product_id','product_category','loyalty_score']].groupby(['customer_id','product_id','product_category','loyalty_score']).size().reset_index(name='purchase_count')

    return customer_product_details[['customer_id','loyalty_score','product_id','product_category','purchase_count']]

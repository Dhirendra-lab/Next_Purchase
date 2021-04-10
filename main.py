import glob
from src.data_pipeline import report_generation
import pandas as pd

#get all json filename
all_files = glob.glob(r'INPUT\transactions\*\*.json')

# Read customers &  products files1
customer_data = pd.read_csv(r'INPUT\customers.csv')
products_data = pd.read_csv(r'INPUT\products.csv')

# calling report generation function
customer_product_details=report_generation(all_files,customer_data,products_data)

customer_product_details.to_csv('OUTPUT/OutPut_Report.csv',index = False)

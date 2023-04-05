import pandas as pd
from validate_xemail import validateEmail

# read the CSV or Excel file
df = pd.read_csv('emails.csv')
# or df = pd.read_excel('emails.xlsx')
validate_email=validateEmail.validate
# create a new column to store the validation result
df['valid'] = ''

# loop through each email and verify it
for index, row in df.iterrows():
    if validate_email(row['email']):
        df.at[index, 'valid'] = 'valid'
    else:
        df.at[index, 'valid'] = 'invalid'

# write the results to a new CSV or Excel file
df.to_csv('verified_emails.csv', index=False)
# or df.to_excel('verified_emails.xlsx', index=False)
print("done")
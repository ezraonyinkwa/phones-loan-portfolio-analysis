#--------------------Customer Data date of birth preparation--------------------
#Extract only the date part from the datetime column
customer_dob['date_of_birth'] = customer_dob['date_of_birth'].dt.date

#Calculate age from date of birth
today = dt.date.today()
customer_dob['age'] = customer_dob['date_of_birth'].apply(lambda x: (today - x).days // 365 if pd.notnull(x) else None)

#Group ages into age groups
bins = [0, 18, 25, 35, 45, 55, 65, float('inf')]
labels = ['0-18', '19-25', '26-35', '36-45', '46-55', '56-65', '65+']
customer_dob['age_group'] = pd.cut(customer_dob['age'], bins=bins, labels=labels, right=False)  

#Quality check after age group creation
customer_dob['age_group'].value_counts()

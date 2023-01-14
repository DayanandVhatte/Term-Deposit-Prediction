import pickle
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

model = pickle.load(open('Gradient_Boosting.pickle','rb'))

project_data = {"marital":{"married":1,"single":2,"divorced":0},
                "housing":{"no":0,"yes":1},
                "loan":{"no":0,"yes":1},
                "contact":{"cellular":0,"telephone":1,"unknown":2}}

col = ['age', 'marital', 'balance', 'housing', 'loan', 'contact', 'day',
       'duration', 'campaign', 'previous', 'job_admin.',
       'job_blue-collar', 'job_entrepreneur', 'job_housemaid',
       'job_management', 'job_retired', 'job_self-employed', 'job_services',
       'job_student', 'job_technician', 'job_unemployed', 'job_unknown',
       'education_primary', 'education_secondary', 'education_tertiary',
       'education_unknown', 'month_apr', 'month_aug', 'month_dec', 'month_feb',
       'month_jan', 'month_jul', 'month_jun', 'month_mar', 'month_may',
       'month_nov', 'month_oct', 'month_sep', 'poutcome_failure',
       'poutcome_other', 'poutcome_success', 'poutcome_unknown']


def deposite(age, marital, balance, housing, loan, contact, day, duration, campaign, previous, job, education, month, poutcome):
    
    if ("job_"+job) in col:
        data = "job_"+job
        index1 = col.index(data)
    if ("education_"+education) in col:
        data = "education_"+education
        index2 = col.index(data)
    if ("month_"+month) in col:
        data = "month_"+month
        index3 = col.index(data)
    if ("poutcome_"+poutcome) in col:
        data = "poutcome_"+poutcome
        index4 = col.index(data)
    
    

    
    test = np.zeros(42)
    test[0] = age
    test[1] = project_data['marital'][marital] 
    test[3] = balance
    test[4] = project_data['housing'][housing]
    test[5] = project_data['loan'][loan]
    test[6] = project_data['contact'][contact]
    test[7] = day
    test[8] = duration
    test[9] = campaign
    test[10] = previous
    test[index1] = 1
    test[index2] = 1
    test[index3] = 1
    test[index4] = 1

    
    data = pd.DataFrame(data=[test])
    
    subscription = model.predict(data.values)
    
    return subscription

     
       
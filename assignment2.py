import pandas as pd
import numpy as np

# load gapminder dataset
data = pd.read_csv('gapminder.csv',low_memory=False)
# lower-case all DataFrame column names
data.columns = map(str.lower, data.columns)
# bug fix for display formats to avoid run time errors
pd.set_option('display.float_format', lambda x:'%f'%x)

# setting variables to be numeric
data['suicideper100th'] = data['suicideper100th'].convert_objects(convert_numeric=True)
data['breastcancerper100th'] = data['breastcancerper100th'].convert_objects(convert_numeric=True)
data['hivrate'] = data['hivrate'].convert_objects(convert_numeric=True)
data['employrate'] = data['employrate'].convert_objects(convert_numeric=True)

# display summary statistics about the data
print("Statistics for a Suicide Rate")
print(data['suicideper100th'].describe())

# subset data for a high suicide rate based on summary statistics
sub = data[(data['suicideper100th']>12)]
#make a copy of my new subsetted data
sub_copy = sub.copy()

# BREAST CANCER RATE
# frequency and percentage distritions for a number of breast cancer cases with a high suicide rate
#print('frequency for a number of breast cancer cases with a high suicide rate')
bc = sub_copy['breastcancerper100th'].value_counts(sort=False,bins=10)
#print(bc)

#print('percentage for a number of breast cancer cases with a high suicide rate')
pbc = sub_copy['breastcancerper100th'].value_counts(sort=False,bins=10,normalize=True)*100
#print(pbc)

# cumulative frequency and cumulative percentage for a number of breast cancer cases with a high suicide rate
bc1=[] # Cumulative Frequency
pbc1=[] # Cumulative Percentage
cf=0
cp=0
for freq in bc:
    cf=cf+freq
    bc1.append(cf)    
    pf=cf*100/len(sub_copy)
    pbc1.append(pf)
#print('cumulative frequency for a number of breast cancer cases with a high suicide rate')
#print(bc1)
#print('cumulative percentage for a number of breast cancer cases with a high suicide rate')
#print(pbc1)

print('Number of Breast Cancer Cases with a High Suicide Rate')
fmt1 = '%s %7s %9s %12s %12s'
fmt2 = '%5.2f %10.d %10.2f %10.d %12.2f'
print(fmt1 % ('# of Cases','Freq.','Percent','Cum. Freq.','Cum. Percent'))
for i, (key, var1, var2, var3, var4) in enumerate(zip(bc.keys(),bc,pbc,bc1,pbc1)):
    print(fmt2 % (key, var1, var2, var3, var4))
fmt3 = '%5s %10s %10s %10s %12s'   
print(fmt3 % ('NA', '2', '3.77', '53', '100.00'))


# HIV RATE
# frequency and percentage distritions for HIV rate with a high suicide rate
#print('frequency for HIV rate with a high suicide rate')
hc = sub_copy['hivrate'].value_counts(sort=False,bins=7)
#print(hc)

#print('percentage for HIV rate with a high suicide rate')
phc = sub_copy['hivrate'].value_counts(sort=False,bins=7,normalize=True)*100
#print(phc)

# cumulative frequency and cumulative percentage for HIV rate with a high suicide rate
hc1=[] # Cumulative Frequency
phc1=[] # Cumulative Percentage
cf=0
cp=0
for freq in bc:
    cf=cf+freq
    hc1.append(cf)    
    pf=cf*100/len(sub_copy)
    phc1.append(pf)
#print('cumulative frequency for HIV rate with a high suicide rate')
#print(hc1)
#print('cumulative percentage for HIV rate with a high suicide rate')
#print(phc1)

print('HIV Rate with a High Suicide Rate')
fmt1 = '%5s %12s %9s %12s %12s'
fmt2 = '%5.2f %10.d %10.2f %10.d %12.2f'
print(fmt1 % ('Rate','Freq.','Percent','Cum. Freq.','Cum. Percent'))
for i, (key, var1, var2, var3, var4) in enumerate(zip(hc.keys(),hc,phc,hc1,phc1)):
    print(fmt2 % (key, var1, var2, var3, var4))
fmt3 = '%5s %10s %10s %10s %12s'   
print(fmt3 % ('NA', '2', '3.77', '53', '100.00'))


# EMPLOYMENT RATE
# frequency and percentage distritions for employment rate with a high suicide rate
#print('frequency for employment rate with a high suicide rate')
ec = sub_copy['employrate'].value_counts(sort=False,bins=10)
#print(ec)

#print('percentage for employment rate with a high suicide rate')
pec = sub_copy['employrate'].value_counts(sort=False,bins=10,normalize=True)*100
#print(pec)

# cumulative frequency and cumulative percentage for employment rate with a high suicide rate
ec1=[] # Cumulative Frequency
pec1=[] # Cumulative Percentage
cf=0
cp=0
for freq in bc:
    cf=cf+freq
    ec1.append(cf)    
    pf=cf*100/len(sub_copy)
    pec1.append(pf)
#print('cumulative frequency for employment rate with a high suicide rate')
#print(ec1)
#print('cumulative percentage for employment rate with a high suicide rate')
#print(pec1)

print('Employment Rate with a High Suicide Rate')
fmt1 = '%5s %12s %9s %12s %12s'
fmt2 = '%5.2f %10.d %10.2f %10.d %12.2f'
print(fmt1 % ('Rate','Freq.','Percent','Cum. Freq.','Cum. Percent'))
for i, (key, var1, var2, var3, var4) in enumerate(zip(ec.keys(),ec,pec,ec1,pec1)):
    print(fmt2 % (key, var1, var2, var3, var4))
fmt3 = '%5s %10s %10s %10s %12s'   
print(fmt3 % ('NA', '2', '3.77', '53', '100.00'))

# END

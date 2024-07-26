clear all

global folder "C:\Users\Acer\Downloads"

import excel "C:\Users\Acer\OneDrive\Desktop\finaldatasetgrouprojectba.xlsx", sheet("Sheet1") firstrow

bro

rename missing_temp treatment
reg proba treatment i.after intera gender_enc location_enc educ_enc i.id, r

encode gender, gen(gender_enc)
encode location, gen(location_enc)
encode age_ordered, gen(age_enc)
encode education, gen(educ_enc)

gen intera = after * treatment

drop gender location education

tab 	gender, gen(gender_)
tab 	age_ordered, gen(age_)
tab 	location, gen(location_)



preserve
keep if after == 0
iebaltab age_1 age_2 age_3 age_4 gender_1 gender_2 location_1 location_2 proba,
grpvar(treatment) savexlsx(bt.xlsx)  replace
restore
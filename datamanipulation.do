clear all

global folder "C:\Users\Acer\Downloads"

import excel "C:\Users\Acer\Downloads\BA_group_project_surveydata.xlsx", sheet("BA_group_project_surveydata") cellrange(A2:BT143) firstrow clear

preserve
gen random_number = runiform()
sort random_number
list in 1/10
restore


drop StartDate EndDate ResponseType IPAddress Progress Durationinseconds Finished RecordedDate ResponseID RecipientLastName RecipientFirstName  RecipientEmail ExternalDataReference LocationLatitude LocationLongitude DistributionChannel

rename Whatisyourage age
rename Whatisyourgender gender
rename Wheredoyoulivecurrently location
rename Inwhatfieldisyoureducation education
rename Whenlookingforajobdoyouv cont

egen age_ordered = group(age), label
label define age_ordered_label 1 "<18" 2 "18-21" 3 "22-25" 4 ">25"
label values age_ordered age_ordered_label

label define gender_label 1 "Male" 2 "Female" 3 "Non Bynary"
label values gender gender_label

recode education 4 = 1
recode education 3 = 2
label define edu_label 1 "No Stem" 2 "Stem"
label values education edu_label

label define location_label 1 "Italy" 2 "Abroad"
label values location location_label

//stem analysis 
preserve 
tab education

drop if education != 2


rename SupposethatMarioRossiislook cont_stem_cons
rename AD cont_stem_da
rename AE cont_stem_ds

egen cont_stem = rowmean(cont_stem_cons cont_stem_da cont_stem_ds)
egen hard_stem_py = rowmean(NowsupposethatMarioimproves AG AH)
egen hard_stem_rsql = rowmean(AI AJ AK)
egen hard_stem_ex = rowmean(AL AM AN)
egen soft_stem_lead = rowmean(AO AP AQ)
egen soft_stem_comm = rowmean(AR AS AT)
egen soft_stem_ps = rowmean(AU AV AW)


gen 	treatment = 0
replace treatment = 1 if hard_stem_rsql!=.
replace treatment = 1 if hard_stem_ex!=.
replace treatment = 1 if hard_stem_py!=.
egen proba = rowmean(hard_stem_py hard_stem_rsql hard_stem_ex soft_stem_lead soft_stem_comm soft_stem_ps)

gen prob_diff = proba-cont_stem

keep prob_diff proba cont_stem treatment age_ordered gender location education

reg prob_diff i.treatment age_ordered gender location, r

gen id = _n

expand 2
by id, sort: gen after = (_n==1)
replace proba = cont_stem if after == 0


keep id gender location age_ordered treatment after proba education
order id gender location age_ordered treatment after proba
reg proba  i.treatment i.after i.treatment##i.after gender location age_ordered i.id, r

gsort -after +id

keep proba  after treatment gender location age_ordered id
order proba   after treatment gender location age_ordered id
gen random_number = runiform()
sort random_number
drop random_number
list in 1/10


restore

bro

//business analysis

preserve 

drop if education == 2


egen cont_bus = rowmean(AX AY AZ)
egen hard_bus_py = rowmean(BA BB BC)
egen hard_bus_rsql = rowmean(BD BE BF)
egen hard_bus_ex = rowmean(BG BH BI)
egen soft_bus_lead = rowmean(BJ BK BL)
egen soft_bus_comm = rowmean(BM BN BO)
egen soft_bus_ps = rowmean(BP BQ BR)

bro
gen 	treatment = 0
replace treatment = 1 if hard_bus_py!=.
replace treatment = 1 if hard_bus_rsql!=.
replace treatment = 1 if hard_bus_ex!=.
egen proba = rowmean(hard_bus_py hard_bus_rsql hard_bus_ex soft_bus_lead soft_bus_comm soft_bus_ps)

gen id = _n

expand 2
by id, sort: gen after = (_n==1)
replace proba = cont_bus if after == 0


keep id gender location age_ordered treatment after proba education
order id gender location age_ordered treatment after proba
reg proba  i.treatment i.after i.treatment##i.after gender location age_ordered i.id, r

gsort -after +id

restore
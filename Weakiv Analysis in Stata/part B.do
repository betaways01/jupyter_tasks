clear
import excel "C:\Users\HP\Desktop\WORKsz\Fiverr\Aneesa_Econ\Data for part B.xlsx", sheet("Data_to_Use") cellrange(A5:I250) firstrow
drop B H
summarize
// format date
format %tdCCYY-NN-DD Observation_date

// selecting time frames
gen subset =.
// before 1984 (subset 1)
replace subset = 1 if Observation_date < td(01jan1984)
//between 1984 and 2007 (subset 2)
replace subset = 2 if Observation_date >= td(01jan1984) & Observation_date <= td(01oct2007)
//between 2008 and 2021(subset 3).
replace subset = 3  if Observation_date >= td(01jan2008)

// generating lags
gen inflation_lagp1 = inflation[_n+1]
gen inflation_lag1 = inflation[_n-1]

// modelling the  New Keynesian Phillips curve equation
// subset 1
ivreg2 inflation inflation_lagp1 inflation_lag1 (outputgap = Changeininflation growthrate mc_scaled ) if subset ==1
weakiv ivreg2 inflation inflation_lagp1 inflation_lag1 (outputgap = Changeininflation growthrate mc_scaled ) if subset ==1, graph(wald ar)

// subset 2
ivreg2 inflation inflation_lagp1 inflation_lag1 (outputgap = Changeininflation growthrate mc_scaled ) if subset ==2
weakiv ivreg2 inflation inflation_lagp1 inflation_lag1 (outputgap = Changeininflation growthrate mc_scaled ) if subset ==2, graph(wald ar)

// subset 3
ivreg2 inflation inflation_lagp1 inflation_lag1 (outputgap = Changeininflation growthrate mc_scaled ) if subset ==3
weakiv ivreg2 inflation inflation_lagp1 inflation_lag1 (outputgap = Changeininflation growthrate mc_scaled ) if subset ==3, graph(wald ar)

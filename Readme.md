
In this challenge, we firstly use log-return to nomorlize the price data. Then, used relations-network graphs in Azure and obtain the potential predictable groups, then we used HISC features selection method to do the further feature selection. In predicting parts, we used a gradient boosting classifier to train a machine learning model to predict the increasement or decreasement in the next 20 days for our selected predictable financial instruments. we sucessfully trained our model which has a 68.75% accurcy of predicting test datasets. Futhermore, we model a Binomial-Levy stable model to measure the distributions of expected loss of our predicting model for model evaluation and risk control.

The code and output can be found at jupyter notebook.  

Raw_data_clean is used to trans data from long_type to wide_type

![image](https://github.com/HaoranXue/UCL-data-science-challenge/blob/master/net_work.png)

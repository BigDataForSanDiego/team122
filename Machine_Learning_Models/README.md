We collect the data and train our model primarily based on CDC Behavioral Risk Factor Surveillance System https://www.cdc.gov/brfss/index.html. There is a summary for each model in the folder. 
- (1) A machine learning model predict whether the patient is healthy, diabites, heart disease or both ~50% accuracy (dataset: CDC BRFSS 2015). 
- (2) A machine learning model predict the chance the patient having diabites ~72% accuracy (dataset: CDC BRFSS 2021).
- (3) A machine learning model predict the chance the patient having heart disease ~75% accuracy (dataset: CDC BRFSS 2021). 
- (4) A machine learning model predict the patient has flu/covid/cold/allergy ~94% accuracy (interactive).


Patient -> Fillout basic screening questions (or set of questions given by hospital) -> Model 1 process -> If patient have higher chance of diabites -> Direct patient to 2nd model (or 3rd model if higher chance of heart disease).

Our long term vision is build a machine learning model that can help detect all posible diseases. 

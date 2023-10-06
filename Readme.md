# Predictive Model for Early Adoption of Pets within the First Month on Petfinder

## Business Problem:  
How can we utilize the available metadata from online pet profiles on PetFinder.my to develop predictive algorithms that assess the likelihood of a pet being adopted quickly? An effective solution will not only support shelters and rescuers in optimizing their pet profiles but also assist adoption centers and individuals in anticipating the duration of pets' stays. This predictive insight will aid in planning for their stay, estimating food requirements, and potentially seeking foster homes for them until permanent adoption. The overarching goal is to reduce animal suffering and euthanization rates while improving operational efficiency for adoption centers.

## Dataset:  
The data I used for this exercise is sourced from pet listings on PetFinder that has been posted as a [Kaggle challenge](https://www.kaggle.com/competitions/petfinder-adoption-prediction/data). It includes 14993 classified into 5 groups according to their adoption speed.  
for the purpose of this excercise I reclassified the data into just two classes:  
- **class 1** - Adopted within 1 month of listing
- **class 0** - Not adopted within 1 month of listing

While the original dataset encompasses text, tabular, and image data formats, for the purpose of this exercise, only the tabular data will be utilized.  

Below is the description of the data columns:  
### Target Value Description:
AdoptionSpeed: Categorical speed of adoption. Lower is faster. This is the value to predict.

### Variables Description:

- **Type** - Type of animal 
  - 1 = Dog
  - 2 = Cat
  
- **Name** - Name of pet (Empty if not named)

- **Age** - Age of pet when listed, in months

- **Breed1, Breed2** - Primary and Secondary breed of pet (if mixed)
  * Refer to BreedLabels dictionary

- **Gender** - Gender of pet
  - 1 = Male
  - 2 = Female
  - 3 = Mixed (if profile represents group of pets)

- **Color1, Color2, Color3** 
  * Refer to ColorLabels dictionary

- **MaturitySize** - Size at maturity
  - 1 = Small
  - 2 = Medium
  - 3 = Large
  - 4 = Extra Large
  - 0 = Not Specified

- **FurLength** - Fur length
  - 1 = Short
  - 2 = Medium
  - 3 = Long
  - 0 = Not Specified

- **Vaccinated** - Pet has been vaccinated 
  - 1 = Yes
  - 2 = No
  - 3 = Not Sure

- **Dewormed** - Pet has been dewormed
  - 1 = Yes
  - 2 = No
  - 3 = Not Sure

- **Sterilized** - Pet has been spayed / neutered
  - 1 = Yes
  - 2 = No
  - 3 = Not Sure

- **Health** - Health Condition 
  - 1 = Healthy
  - 2 = Minor Injury
  - 3 = Serious Injury
  - 0 = Not Specified

- **Quantity** - Number of pets represented in profile

- **Fee** - Adoption fee (0 = Free)

- **VideoAmt** - Total uploaded videos for this pet

- **PhotoAmt** - Total uploaded photos for this pet

It's worth noting that occasionally, a single profile might represent a group of pets; in such instances, the adoption speed is gauged based on the time taken for the entire group of pets to be adopted.


## Methods

For this project, given the binary nature of the target variable, I primarily focused on two classification algorithms: Decision Trees and Logistic Regression.

1. **Decision Tree (Baseline Model):** I initiated with a Decision Tree as the baseline model to set a foundational benchmark for performance.
   
2. **Tuned Decision Tree:** Building upon the baseline, I proceeded to fine-tune the hyperparameters of the Decision Tree, aiming for enhanced predictive capabilities.
   
3. **Logistic Regression:** To diversify and potentially refine our predictions, I implemented the Logistic Regression model.
   
4. **Tuned Logistic Regression:** To further optimize our results, the Logistic Regression model underwent hyperparameter tuning, ensuring peak accuracy in predictions.

5. **Feature Importance Evaluation:** I picked the best model of the 4, which is the tuned Decision tree, and checked the feature importance.

6. **Refined Model with Selected Features:** I picked the top 10 features from the tuned Decision tree model and trained a refined model with only these 10 features. the results were very similar to those of the tuned model, using only 10 columns instead of 24. This might not make a big difference on the processing time for this model, but for a bigger data it will save a lot of processing power and time.


### Evaluation Metric:

For the assessment of our models, we will primarily utilize the **accuracy** metric. This choice stems from our objective where both positive and negative outcomes are of equal importance to us. Thus, a model's ability to correctly predict overall instances, whether positive or negative, is pivotal in determining its effectiveness.


## Results:  
1. **Decision Tree (Baseline Model):**  
Accuracy on train data: 0.99  
Accuracy on test data: 0.59
<table>
<tr>
<td>
<img src="https://github.com/alihijazy/Predictive-Model-for-Early-Adoption-of-Pets-within-the-First-Month-on-Petfinder/blob/master/Pictures/Baseline%20model.png" alt="Alt Text 1" width="100%"/>
</td>
<td>
<img src="https://github.com/alihijazy/Predictive-Model-for-Early-Adoption-of-Pets-within-the-First-Month-on-Petfinder/blob/master/Pictures/Decision%20tree%20(Baseline%20model)%20confusion%20matrix.png" alt="Alt Text 2" width="100%"/>
</td>
</tr>
</table>
<img src="https://github.com/alihijazy/Predictive-Model-for-Early-Adoption-of-Pets-within-the-First-Month-on-Petfinder/blob/master/Pictures/Decision%20Tree%20Plot.png">

2. **Tuned Decision Tree:**  
Accuracy on train data: 0.65  
Accuracy on test data: 0.63
<table>
<tr>
<td>
<img src="https://github.com/alihijazy/Predictive-Model-for-Early-Adoption-of-Pets-within-the-First-Month-on-Petfinder/blob/master/Pictures/Tuned%20Decision%20Tree%20Model.png" alt="Alt Text 1" width="100%"/>
</td>
<td>
<img src="https://github.com/alihijazy/Predictive-Model-for-Early-Adoption-of-Pets-within-the-First-Month-on-Petfinder/blob/master/Pictures/Tuned%20Decision%20Tree%20Model%20Confusion%20Matrix.png" alt="Alt Text 2" width="100%"/>
</td>
</tr>
</table>   
<img src="https://github.com/alihijazy/Predictive-Model-for-Early-Adoption-of-Pets-within-the-First-Month-on-Petfinder/blob/master/Pictures/Tuned%20Decision%20Tree%20Plot.png">

3. **Logistic Regression:**  
Accuracy on train data: 0.59  
Accuracy on test data: 0.58
<table>
<tr>
<td>
<img src="https://github.com/alihijazy/Predictive-Model-for-Early-Adoption-of-Pets-within-the-First-Month-on-Petfinder/blob/master/Pictures/Logistic%20regression%20model.png" alt="Alt Text 1" width="100%"/>
</td>
<td>
<img src="https://github.com/alihijazy/Predictive-Model-for-Early-Adoption-of-Pets-within-the-First-Month-on-Petfinder/blob/master/Pictures/Logistic%20Regression%20Model%20confusion%20matrix.png" alt="Alt Text 2" width="100%"/>
</td>
</tr>
</table>   

4. **Tuned Logistic Regression:**  
Accuracy on train data: 0.59  
Accuracy on test data: 0.59
<table>
<tr>
<td>
<img src="https://github.com/alihijazy/Predictive-Model-for-Early-Adoption-of-Pets-within-the-First-Month-on-Petfinder/blob/master/Pictures/Tuned%20Logistoc%20Regression.png" alt="Alt Text 1" width="100%"/>
</td>
<td>
<img src="https://github.com/alihijazy/Predictive-Model-for-Early-Adoption-of-Pets-within-the-First-Month-on-Petfinder/blob/master/Pictures/Tuned%20Logistic%20Regression%20Confision%20Matrix.png" alt="Alt Text 2" width="100%"/>
</td>
</tr>
</table>   

5. **Feature Importance Evaluation:**  
I picked the 10 features with the highest feature importance from the tuned decision tree model and reran the model with only these features to save processing power and time. below are the features:  
**Age, Breed1, PhotoAmt, Quantity, Breed2, Sterilized, Gender, Fee, Furlength, and Color1**  

8. **Refined Model with Selected Features:**  
Accuracy on train data: 0.63  
Accuracy on test data: 0.63
<table>
<tr>
<td>
<img src="https://github.com/alihijazy/Predictive-Model-for-Early-Adoption-of-Pets-within-the-First-Month-on-Petfinder/blob/master/Pictures/Refined%20Decision%20Tree.png" alt="Alt Text 1" width="100%"/>
</td>
<td>
<img src="https://github.com/alihijazy/Predictive-Model-for-Early-Adoption-of-Pets-within-the-First-Month-on-Petfinder/blob/master/Pictures/Refined%20Decision%20Tree%20Confision%20Matrix.png" alt="Alt Text 2" width="100%"/>
</td>
</tr>
</table>   
<img src="https://github.com/alihijazy/Predictive-Model-for-Early-Adoption-of-Pets-within-the-First-Month-on-Petfinder/blob/master/Pictures/Refined%20Decision%20Tree%20Plot.png">  

## Conclusion  
**Our best performing model is the refined decision tree model. It scores 63% accuracy and uses only 10 features unlike any other model we tried. so it will require less processing with a bigger dataset.**  

### Recommendations  
- Put this model in use to help know in advance the pets that won’t be adopted soon. Knowing in advance will help plan for their shelters food etc.  

- Give more exposure to the profiles of pets will lower chances of being adopted within a month.  

- Try to adjust the profiles of pets with less chances to make them more desirable (adding more and better pictures, videos)

### Next steps  
include image processing since the picture of the pet can be a main factor of getting them adopted

## Repository Structure
```none            
├── data 
├── Pictures                   
├── .gitignore
├── Readme.md 
├── Pet adoption predictive model.ipynb.ipynb
└── pres-pet-adoption-speed.pdf
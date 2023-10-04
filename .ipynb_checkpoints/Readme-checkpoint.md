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

5. **Feature Importance Evaluation:** After tuning both models, I evaluated the feature importance for each. By identifying and cross-referencing the significant features from both models, I extracted the common influential features.

6. **Refined Model with Selected Features:** Leveraging these common important features, I trained a more streamlined model. The objective was to maintain, if not improve, the accuracy of predictions while utilizing fewer columns. This approach not only boosts model efficiency but also reduces processing time and computational powerequirements.


### Evaluation Metric:

For the assessment of our models, we will primarily utilize the **accuracy** metric. This choice stems from our objective where both positive and negative outcomes are of equal importance to us. Thus, a model's ability to correctly predict overall instances, whether positive or negative, is pivotal in determining its effectiveness.


## Results:  
1. **Decision Tree (Baseline Model):**
Accuracy on train data: 0.99  
Accuracy on test data: 0.58
<table>
<tr>
<td>
<img src="https://github.com/alihijazy/Predictive-Model-for-Early-Adoption-of-Pets-within-the-First-Month-on-Petfinder/blob/master/Pictures/Baseline%20model.png" alt="Alt Text 1" width="100%"/>
</td>
<td>
<img src="https://github.com/alihijazy/Predictive-Model-for-Early-Adoption-of-Pets-within-the-First-Month-on-Petfinder/blob/master/Pictures/Baseline%20model%20confusion%20matrix.png" alt="Alt Text 2" width="100%"/>
</td>
</tr>
</table>
<img src="https://github.com/alihijazy/Predictive-Model-for-Early-Adoption-of-Pets-within-the-First-Month-on-Petfinder/blob/master/Pictures/Decision%20Tree%20Plot.png">

2. **Tuned Decision Tre3:** 
Accuracy on train data: 0.66  
Accuracy on test data: 0.64
<table>
<tr>
<td>
<img src="https://github.com/alihijazy/Predictive-Model-for-Early-Adoption-of-Pets-within-the-First-Month-on-Petfinder/blob/master/Pictures/Tuned%20Baseline%20Model.png" alt="Alt Text 1" width="100%"/>
</td>
<td>
<img src="https://github.com/alihijazy/Predictive-Model-for-Early-Adoption-of-Pets-within-the-First-Month-on-Petfinder/blob/master/Pictures/Tuned%20Baseline%20Model%20confusion%20matrix.png" alt="Alt Text 2" width="100%"/>
</td>
</tr>
</table>   
<img src="https://github.com/alihijazy/Predictive-Model-for-Early-Adoption-of-Pets-within-the-First-Month-on-Petfinder/blob/master/Pictures/Tuned%20Decision%20Tree%20Plot.png">

4. **Logistic Regressio4:** 
   
5. **Tuned Logistic Regres5ion:** 

6. **Feature Importance Evalua6ion:** 

7. **Refined Model with Selected Features:** 

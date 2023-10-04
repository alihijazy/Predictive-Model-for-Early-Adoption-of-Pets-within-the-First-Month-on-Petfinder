{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "2dd36739-6b06-496c-b4b8-fc3facd68ecc",
   "metadata": {},
   "source": [
    "# Predictive Model for Early Adoption of Pets within the First Month on Petfinder"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "892d5056-45e5-48c8-86cb-c7c7c35c3907",
   "metadata": {},
   "source": [
    "## Business Problem:  \n",
    "How can we utilize the available metadata from online pet profiles on PetFinder.my to develop predictive algorithms that assess the likelihood of a pet being adopted quickly? An effective solution will not only support shelters and rescuers in optimizing their pet profiles but also assist adoption centers and individuals in anticipating the duration of pets' stays. This predictive insight will aid in planning for their stay, estimating food requirements, and potentially seeking foster homes for them until permanent adoption. The overarching goal is to reduce animal suffering and euthanization rates while improving operational efficiency for adoption centers."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d7d99c68-6d22-4b62-aa42-3b95161a0cc9",
   "metadata": {},
   "source": [
    "## Dataset:  \n",
    "The data I used for this exercise is sourced from pet listings on PetFinder that has been posted as a [Kaggle challenge](https://www.kaggle.com/competitions/petfinder-adoption-prediction/data). It includes 14993 classified into 5 groups according to their adoption speed.  \n",
    "for the purpose of this excercise I reclassified the data into just two classes:  \n",
    "- **class 1** - Adopted within 1 month of listing\n",
    "- **class 0** - Not adopted within 1 month of listing\n",
    "\n",
    "While the original dataset encompasses text, tabular, and image data formats, for the purpose of this exercise, only the tabular data will be utilized.  \n",
    "\n",
    "Below is the description of the data columns:  \n",
    "### Target Value Description:\n",
    "AdoptionSpeed: Categorical speed of adoption. Lower is faster. This is the value to predict.\n",
    "\n",
    "### Variables Description:\n",
    "\n",
    "- **Type** - Type of animal \n",
    "  - 1 = Dog\n",
    "  - 2 = Cat\n",
    "  \n",
    "- **Name** - Name of pet (Empty if not named)\n",
    "\n",
    "- **Age** - Age of pet when listed, in months\n",
    "\n",
    "- **Breed1, Breed2** - Primary and Secondary breed of pet (if mixed)\n",
    "  * Refer to BreedLabels dictionary\n",
    "\n",
    "- **Gender** - Gender of pet\n",
    "  - 1 = Male\n",
    "  - 2 = Female\n",
    "  - 3 = Mixed (if profile represents group of pets)\n",
    "\n",
    "- **Color1, Color2, Color3** \n",
    "  * Refer to ColorLabels dictionary\n",
    "\n",
    "- **MaturitySize** - Size at maturity\n",
    "  - 1 = Small\n",
    "  - 2 = Medium\n",
    "  - 3 = Large\n",
    "  - 4 = Extra Large\n",
    "  - 0 = Not Specified\n",
    "\n",
    "- **FurLength** - Fur length\n",
    "  - 1 = Short\n",
    "  - 2 = Medium\n",
    "  - 3 = Long\n",
    "  - 0 = Not Specified\n",
    "\n",
    "- **Vaccinated** - Pet has been vaccinated \n",
    "  - 1 = Yes\n",
    "  - 2 = No\n",
    "  - 3 = Not Sure\n",
    "\n",
    "- **Dewormed** - Pet has been dewormed\n",
    "  - 1 = Yes\n",
    "  - 2 = No\n",
    "  - 3 = Not Sure\n",
    "\n",
    "- **Sterilized** - Pet has been spayed / neutered\n",
    "  - 1 = Yes\n",
    "  - 2 = No\n",
    "  - 3 = Not Sure\n",
    "\n",
    "- **Health** - Health Condition \n",
    "  - 1 = Healthy\n",
    "  - 2 = Minor Injury\n",
    "  - 3 = Serious Injury\n",
    "  - 0 = Not Specified\n",
    "\n",
    "- **Quantity** - Number of pets represented in profile\n",
    "\n",
    "- **Fee** - Adoption fee (0 = Free)\n",
    "\n",
    "- **VideoAmt** - Total uploaded videos for this pet\n",
    "\n",
    "- **PhotoAmt** - Total uploaded photos for this pet\n",
    "\n",
    "It's worth noting that occasionally, a single profile might represent a group of pets; in such instances, the adoption speed is gauged based on the time taken for the entire group of pets to be adopted.\r\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9d8da4fe-d4f3-4d10-9b20-faa7d0df454d",
   "metadata": {},
   "source": [
    "## Methods\r\n",
    "\r\n",
    "For this project, given the binary nature of the target variable, I primarily focused on two classification algorithms: Decision Trees and Logistic Regression.\r\n",
    "\r\n",
    "1. **Decision Tree (Baseline Model):** I initiated with a Decision Tree as the baseline model to set a foundational benchmark for performance.\r\n",
    "   \r\n",
    "2. **Tuned Decision Tree:** Building upon the baseline, I proceeded to fine-tune the hyperparameters of the Decision Tree, aiming for enhanced predictive capabilities.\r\n",
    "   \r\n",
    "3. **Logistic Regression:** To diversify and potentially refine our predictions, I implemented the Logistic Regression model.\r\n",
    "   \r\n",
    "4. **Tuned Logistic Regression:** To further optimize our results, the Logistic Regression model underwent hyperparameter tuning, ensuring peak accuracy in predictions.\r\n",
    "\r\n",
    "5. **Feature Importance Evaluation:** After tuning both models, I evaluated the feature importance for each. By identifying and cross-referencing the significant features from both models, I extracted the common influential features.\r\n",
    "\r\n",
    "6. **Refined Model with Selected Features:** Leveraging these common important features, I trained a more streamlined model. The objective was to maintain, if not improve, the accuracy of predictions while utilizing fewer columns. This approach not only boosts model efficiency but also reduces processing time and computational powerequirements.\r\n",
    "\r\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b2dd314e-f478-468d-bca1-fbd0cf3a2788",
   "metadata": {},
   "source": [
    "### Evaluation Metric:\r\n",
    "\r\n",
    "For the assessment of our models, we will primarily utilize the **accuracy** metric. This choice stems from our objective where both positive and negative outcomes are of equal importance to us. Thus, a model's ability to correctly predict overall instances, whether positive or negative, is pivotal in determining its effectiveness.\r\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d3dda473-df85-49e6-952d-c2f50724dbb6",
   "metadata": {},
   "source": [
    "## Results:  \n",
    "1. **Decision Tree (Baseline Model):**\n",
    "\n",
    "2. **\n",
    "   \n",
    "2. **Tuned Decision Tre3:** \n",
    "   \n",
    "4. **Logistic Regressio4:** \n",
    "   \n",
    "5. **Tuned Logistic Regres5ion:** \n",
    "\n",
    "6. **Feature Importance Evalua6ion:** \n",
    "\n",
    "7. **Refined Model with Selected Features:** "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c3ebe1a-d01d-40d4-92a3-262da51e3121",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

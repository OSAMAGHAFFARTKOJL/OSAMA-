from django.shortcuts import render
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from django.http import HttpResponse
from django.http import JsonResponse

    

def hello(request):
    
    
    
    if request.method == 'POST':
        # Get user input from the form
        pregnant_val = request.POST.get('pregnancy')
        insulin_val = request.POST.get('insulin')
        bmi_val = request.POST.get('bmi')
        age_val = request.POST.get('age')
        glucose_val = request.POST.get('glucose')
        bp_val = request.POST.get('bp')
        pedigree_val = request.POST.get('pedigree')

        # Check if any of the form fields is None, indicating missing input
        if None in (pregnant_val, insulin_val, bmi_val, age_val, glucose_val, bp_val, pedigree_val):
            result = "Please fill out all the fields."
        else:
            # Continue with processing if all inputs are provided
            # Load the dataset (assuming "diabetes.csv" is the dataset you have)
            col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
            pima = pd.read_csv("data/diabetes.csv", header=0, names=col_names)
            pima = pima[100:]  # You can keep this line to remove the first 100 rows if needed

            # Define feature columns and target variable
            feature_cols = ['pregnant', 'insulin', 'bmi', 'age', 'glucose', 'bp', 'pedigree']
            X = pima[feature_cols]  # Features
            y = pima.label  # Target variable

            clf = DecisionTreeClassifier(max_depth=3, min_samples_split=2, min_samples_leaf=1)
            clf.fit(X, y)

            # Create a list with the user's input data
            user_data = [[int(pregnant_val), int(insulin_val), float(bmi_val), int(age_val), int(glucose_val), int(bp_val), float(pedigree_val)]]

            # Predict whether the user has diabetes or not
            prediction = clf.predict(user_data)

            if prediction[0] == 1:
                result = "You have diabetes."
                #return JsonResponse({"result": result})
            else:
                result = "You do not have diabetes."
                #return JsonResponse({"result": result})

        # Return an HttpResponse object with the result message
    else:
        # Handle GET requests (initial form display)
        result = None

    return render(request, 'cv.html', {'result': result})

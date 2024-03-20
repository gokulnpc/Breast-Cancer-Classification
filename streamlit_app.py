import streamlit as st
import pandas as pd
import joblib
# Function to load the model
@st.cache_data
def load_model():
    with open('model', 'rb') as file:
        loaded_model = joblib.load(file)
    return loaded_model

# Load your model
loaded_model = load_model()


# Sidebar for navigation
st.sidebar.title('Navigation')
options = st.sidebar.selectbox('Select a page:', 
                           ['Prediction', 'Code', 'About'])

if options == 'Prediction': # Prediction page
    st.title('Breast Cancer Classification Web App')


    # User inputs: 
    # Index(['mean radius', 'mean texture', 'mean perimeter', 'mean area',
    #    'mean smoothness', 'mean compactness', 'mean concavity',
    #    'mean concave points', 'mean symmetry', 'mean fractal dimension',
    #    'radius error', 'texture error', 'perimeter error', 'area error',
    #    'smoothness error', 'compactness error', 'concavity error',
    #    'concave points error', 'symmetry error', 'fractal dimension error',
    #    'worst radius', 'worst texture', 'worst perimeter', 'worst area',
    #    'worst smoothness', 'worst compactness', 'worst concavity',
    #    'worst concave points', 'worst symmetry', 'worst fractal dimension'],
    #   dtype='object')
    # intilaize the user inputs
    mean_radius = st.number_input('Mean Radius', min_value=0.0, max_value=30.0, value=15.0)
    mean_texture = st.number_input('Mean Texture', min_value=0.0, max_value=40.0, value=20.0)
    mean_perimeter = st.number_input('Mean Perimeter', min_value=0.0, max_value=200.0, value=100.0)
    mean_area = st.number_input('Mean Area', min_value=0.0, max_value=2500.0, value=500.0)
    mean_smoothness = st.number_input('Mean Smoothness', min_value=0.0, max_value=0.25, value=0.1)
    mean_compactness = st.number_input('Mean Compactness', min_value=0.0, max_value=0.5, value=0.2)
    mean_concavity = st.number_input('Mean Concavity', min_value=0.0, max_value=0.5, value=0.2)
    mean_concave_points = st.number_input('Mean Concave Points', min_value=0.0, max_value=0.2, value=0.1)
    mean_symmetry = st.number_input('Mean Symmetry', min_value=0.0, max_value=0.5, value=0.2)
    mean_fractal_dimension = st.number_input('Mean Fractal Dimension', min_value=0.0, max_value=0.1, value=0.05)
    radius_error = st.number_input('Radius Error', min_value=0.0, max_value=2.0, value=0.5)
    texture_error = st.number_input('Texture Error', min_value=0.0, max_value=5.0, value=2.0)
    perimeter_error = st.number_input('Perimeter Error', min_value=0.0, max_value=20.0, value=5.0)
    area_error = st.number_input('Area Error', min_value=0.0, max_value=200.0, value=50.0)
    smoothness_error = st.number_input('Smoothness Error', min_value=0.0, max_value=0.05, value=0.01)
    compactness_error = st.number_input('Compactness Error', min_value=0.0, max_value=0.1, value=0.02)
    concavity_error = st.number_input('Concavity Error', min_value=0.0, max_value=0.1, value=0.02)
    concave_points_error = st.number_input('Concave Points Error', min_value=0.0, max_value=0.05, value=0.01)
    symmetry_error = st.number_input('Symmetry Error', min_value=0.0, max_value=0.1, value=0.02)
    fractal_dimension_error = st.number_input('Fractal Dimension Error', min_value=0.0, max_value=0.05, value=0.01)
    worst_radius = st.number_input('Worst Radius', min_value=0.0, max_value=40.0, value=20.0)
    worst_texture = st.number_input('Worst Texture', min_value=0.0, max_value=50.0, value=30.0)
    worst_perimeter = st.number_input('Worst Perimeter', min_value=0.0, max_value=300.0, value=150.0)
    worst_area = st.number_input('Worst Area', min_value=0.0, max_value=4000.0, value=1000.0)
    worst_smoothness = st.number_input('Worst Smoothness', min_value=0.0, max_value=0.3, value=0.15)
    worst_compactness = st.number_input('Worst Compactness', min_value=0.0, max_value=1.0, value=0.3)
    worst_concavity = st.number_input('Worst Concavity', min_value=0.0, max_value=1.0, value=0.3)
    worst_concave_points = st.number_input('Worst Concave Points', min_value=0.0, max_value=0.5, value=0.2)
    worst_symmetry = st.number_input('Worst Symmetry', min_value=0.0, max_value=1.0, value=0.3)
    worst_fractal_dimension = st.number_input('Worst Fractal Dimension', min_value=0.0, max_value=0.5, value=0.2)
    

    user_inputs = {
        'mean radius': mean_radius,
        'mean texture': mean_texture,
        'mean perimeter': mean_perimeter,
        'mean area': mean_area,
        'mean smoothness': mean_smoothness,
        'mean compactness': mean_compactness,
        'mean concavity': mean_concavity,
        'mean concave points': mean_concave_points,
        'mean symmetry': mean_symmetry,
        'mean fractal dimension': mean_fractal_dimension,
        'radius error': radius_error,
        'texture error': texture_error,
        'perimeter error': perimeter_error,
        'area error': area_error,
        'smoothness error': smoothness_error,
        'compactness error': compactness_error,
        'concavity error': concavity_error,
        'concave points error': concave_points_error,
        'symmetry error': symmetry_error,
        'fractal dimension error': fractal_dimension_error,
        'worst radius': worst_radius,
        'worst texture': worst_texture,
        'worst perimeter': worst_perimeter,
        'worst area': worst_area,
        'worst smoothness': worst_smoothness,
        'worst compactness': worst_compactness,
        'worst concavity': worst_concavity,
        'worst concave points': worst_concave_points,
        'worst symmetry': worst_symmetry,
        'worst fractal dimension': worst_fractal_dimension
    }
    
    if st.button('Predict'):
        df = pd.DataFrame(user_inputs, index=[0])
        prediction = loaded_model.predict(df)
        
        if prediction[0] == 1:
            st.error('The Breast cancer is Malignant')
        else:
            st.success('The Breast Cancer is Benign')
        
        with st.expander("Show more details"):
            st.write("Details of the prediction:")
            st.json(loaded_model.get_params())
            st.write('Model used: Logistic Regression')
            
elif options == 'Code':
    st.header('Code')
    # Add a button to download the Jupyter notebook (.ipynb) file
    notebook_path = 'Breast_cancer_model.ipynb'
    with open(notebook_path, "rb") as file:
        btn = st.download_button(
            label="Download Jupyter Notebook",
            data=file,
            file_name="Breast_cancer_model.ipynb",
            mime="application/x-ipynb+json"
        )
    st.write('You can download the Jupyter notebook to view the code and the model building process.')
    st.write('--'*50)

    st.header('Data')
    # Add a button to download your dataset
    data_path = 'data.csv'
    with open(data_path, "rb") as file:
        btn = st.download_button(
            label="Download Dataset",
            data=file,
            file_name="breast_cancer_data.csv",
            mime="text/csv"
        )
    st.write('You can download the dataset to use it for your own analysis or model building.')
    st.write('--'*50)

    st.header('GitHub Repository')
    st.write('You can view the code and the dataset used in this web app from the GitHub repository:')
    st.write('[GitHub Repository](https://github.com/gokulnpc/Breast-Cancer-Classification)')
    st.write('--'*50)
    
elif options == 'About':
    st.title('About')
    st.write('This web app is created to classify the Breast Cancer into Benign and Malignant. The model is built using the Logistic Regression algorithm.')
    st.write('--'*50)
    st.write('The web app is open-source. You can view the code and the dataset used in this web app from the GitHub repository:')
    st.write('[GitHub Repository](https://github.com/gokulnpc/Breast-Cancer-Classification)')
    st.write('--'*50)

    st.header('Contact')
    st.write('You can contact me for any queries or feedback:')
    st.write('Email: gokulnpc@gmail.com')
    st.write('LinkedIn: [Gokuleshwaran Narayanan](https://www.linkedin.com/in/gokulnpc/)')
    st.write('--'*50)

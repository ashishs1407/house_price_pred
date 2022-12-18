from setuptools import setup,find_packages
from typing import List

def get_req()-> List[str] :
    pass


setup(
    name = "House_Price_Prediction",
    version= '0.0.1',
    description="This is a Regression Machine Learning project to Predict the House Price.",
    author="Ashish Shimpi",
    author_email="a.shimpi93@gmail.com",
    packages = find_packages(),
    py_modules=[]

)
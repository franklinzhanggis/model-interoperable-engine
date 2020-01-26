#Data : 2019-12-21
#Author : Fengyuan Zhang (Franklin)
#Email : franklinzhang@foxmail.com
#Description : this file aimes to test different kinds of convertion engines

from BMI_OpenGMS_Engine import BMIOpenGMSEngine
import os
import sys

def test_for_bmi_opengms_engine():
    dirname = os.path.dirname(__file__)
    BMIOpenGMSEngine.convertBMI2OpenGMS(dirname + "/heat", "BmiHeat", dirname + "/data/bmi_heat_map_supplement.json")

if __name__ == "__main__":
    test_for_bmi_opengms_engine()
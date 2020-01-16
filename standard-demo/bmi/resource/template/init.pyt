# This code is generated by BMI-OpenGMS-Engine, for more information, please visit 

from $(File) import $(Class)
from modelservicecontext import EModelContextStatus
from modelservicecontext import ERequestResponseDataFlag
from modelservicecontext import ERequestResponseDataMIME
from modelservicecontext import ModelServiceContext
from modeldatahandler import ModelDataHandler
import numpy as np
import sys
import os

def ConvertString2Array(arr_str):
    arr_str = arr_str.replace("]", "")
    arr_str = arr_str.replace("[", "")
    arr = arr_str.split(",")
    arr = list(map(float, arr))
    return arr

def ConvertString2Array2(arr_str):
    arr_str = arr_str.replace(" ", "")
    arr_str = arr_str.replace("],[", "],,[")
    arr = arr_str.split(",,")
    for index in range(len(arr)):
        arr[index] = ConvertString2Array(arr[index])
    return arr

if len(sys.argv) < 4:
    exit()

ms = ModelServiceContext()
ms.onInitialize(sys.argv[1], sys.argv[2], sys.argv[3])
mdh = ModelDataHandler(ms)

ms.onEnterState('BMIRUNNING')

ms.onFireEvent("Init")
ms.onRequestData()
data_source = None
if ms.getRequestDataFlag() == ERequestResponseDataFlag.ERDF_OK:
    if ms.getRequestDataMIME() == ERequestResponseDataMIME.ERDM_RAW_FILE:
        data_source = ms.getRequestDataBody()
    elif ms.getRequestDataMIME() == ERequestResponseDataMIME.ERDM_ZIP_FILE:
        data_source = ms.getRequestDataBody()
else:
    ms.onFinalize()

bimModel = $(Class)()
bimModel.initialize(data_source)

ipts = bimModel.get_input_var_names()
if not isinstance(ipts, tuple):
    ipts = [ipts]
for ipt in ipts:
    ms.onFireEvent("INPUT_" + ipt)
    ms.onRequestData()
    data_source = None
    if ms.getRequestDataFlag() == ERequestResponseDataFlag.ERDF_OK:
        if ms.getRequestDataMIME() == ERequestResponseDataMIME.ERDM_RAW_FILE:
            data_source = ms.getRequestDataBody()
            arr = np.loadtxt(data_source, dtype=float)
            bimModel.set_value(ipt, arr)
        elif ms.getRequestDataMIME() == ERequestResponseDataMIME.ERDM_ZIP_FILE:
            data_source = ms.getRequestDataBody()
    else:
        ms.onFinalize()

bimModel.update()

opts = bimModel.get_output_var_names()

for opt in opts:
    ms.onFireEvent("OUTPUT_" + opt)
    ms.setResponseDataFlag(ERequestResponseDataFlag.ERDF_OK)
    ms.setResponseDataMIME(ERequestResponseDataMIME.ERDM_RAW_FILE)
    odata = bimModel.get_value(opt)

    opt_file = ms.getCurrentDataDirectory() + "output_" + opt + ".dat"
    
    if isinstance(odata, float) or isinstance(odata, int):
        np.savetxt(opt_file, [odata])
    elif type(odata) is np.ndarray:
        np.savetxt(opt_file, odata)
    else:
        f = open(opt_file, "w")
        f.write(str(odata))
        f.close()
    ms.setResponseDataBody(opt_file)

    ms.onResponseData()

bimModel.finalize()

ms.onFinalize()
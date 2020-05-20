# from heat import BmiHeat
# import numpy as np
# import tempfile
# import yaml

# def ConvertString2Array(arr_str):
#     arr_str = arr_str.replace("]", "")
#     arr_str = arr_str.replace("[", "")
#     arr = arr_str.split(",")
#     arr = list(map(float, arr))
#     return arr

# def ConvertString2Array2(arr_str):
#     arr_str = arr_str.replace(" ", "")
#     arr_str = arr_str.replace("],[", "],,[")
#     arr = arr_str.split(",,")
#     for index in range(len(arr)):
#         arr[index] = ConvertString2Array(arr[index])
#     return arr


# with tempfile.NamedTemporaryFile('w', delete=False) as fp:
#     fp.write(yaml.dump({'shape': (5, 4)}))
#     name = fp.name

# bmi_heat = BmiHeat()
# bmi_heat.initialize(name)

# arr = ConvertString2Array("[1.1, 2.1, 1.5, 1.4]")
# print(arr)

# arr = np.array([[1.1, 2.1, 1.5, 1.4], [1.6, 2.1, 3.5, 1.6], [2.8, 1.4, 5.5, 1.4], [2.1, 2.2, 1.3, 1.1], [2.4, 1.8, 1.2, 0.7]])
# arr_s = "[[1.1, 2.1, 1.5, 1.4], [1.6, 2.1, 3.5, 1.6], [2.8, 1.4, 5.5, 1.4], [2.1, 2.2, 1.3, 1.1], [2.4, 1.8, 1.2, 0.7]]"
# arr_o = ConvertString2Array2(arr_s)

# bmi_heat.set_value("plate_surface__temperature", arr)
# grid_num = bmi_heat.get_var_grid("plate_surface__temperature")
# print(bmi_heat.get_var_type("plate_surface__temperature"))
# print(grid_num)
# print(bmi_heat.get_grid_type(grid_num))
# print(bmi_heat.get_grid_size(grid_num))
# print(bmi_heat.get_grid_shape(grid_num))
# print(bmi_heat.get_grid_rank(grid_num))

# f = open("G:\\\\ReleaseHub\\\\ContainerPacking\\\\GeoModelServiceContainer\\\\geo_data\\\\gd_63e0a771-2d12-11ea-9862-db8f894aaf6e.dat", "r")

# f = open("E:\\GitCode\\model-interoperation-engine\\standard-demo\\bmi\\data\\input_plate_surface__temperature.dat", "r")
# content = f.read()
# f.close()

# arr = np.array([[1.1, 2.1, 1.5, 1.4], [1.6, 2.1, 3.5, 1.6], [2.8, 1.4, 5.5, 1.4], [2.1, 2.2, 1.3, 1.1], [2.4, 1.8, 1.2, 0.7]])
# np.savetxt("tmp.dat", arr)
# arr_t = np.loadtxt("tmp.dat", dtype=float)
# print(arr_t)
# # np.save("tmp.dat", arr)

# import json
# f = open("E:\\GitCode\\model-interoperation-engine\\standard-demo\\bmi\\supplement.json", "r")
# js = json.load(f)
# f.close()

# from bmi_frost_number import *
# import os
# import sys
# from permamodel import examples_directory

# bmi_fn = BmiFrostnumberMethod()

# os.chdir("E:\\GitCode\\model-interoperation-engine\\standard-demo\\bmi")

# config = onesite_multiyear_filename = os.path.join(examples_directory, 'Frostnumber_example_timeseries.cfg')
# bmi_fn.initialize(cfg_file=config)

# opts = bmi_fn.get_output_var_names()
# while bmi_fn.model.year < bmi_fn.model.end_year:
#     print(bmi_fn.model.year)
#     for opt in opts:
#         print(opt + "[" + bmi_fn.get_values_at_indices(opt) + "] : " + str(bmi_fn.get_value(opt)))
#     bmi_fn.update()

# bmi_fn.finalize()

# assert bmi_fn.model.output is not None


# year = bmi_fn.model.start_year
# while year < bmi_fn.model.end_year:
#     assert year in bmi_fn.model.output.keys()
#     year += 1


# import tempfile

# tmpDir = tempfile.TemporaryDirectory()

import numpy as np

np.savetxt("tmp.dat", [-26.5])

a = np.array(np.loadtxt("tmp.dat", dtype=float), dtype=np.float32)

print(a)
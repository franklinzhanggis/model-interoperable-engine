from heat import BmiHeat

bmiheatModel = BmiHeat()
bmiheatModel.initialize()

ipts = bmiheatModel.get_input_var_names()
opts = bmiheatModel.get_output_var_names()

for ipt in ipts:
    print(bmiheatModel.get_var_nbytes(ipt))
    print(bmiheatModel.get_var_type(ipt))
    grid = bmiheatModel.get_var_grid(ipt)
    print(bmiheatModel.get_grid_type(grid))
    print(bmiheatModel.get_grid_shape(grid))
    print(bmiheatModel.get_grid_spacing(grid))
    print(bmiheatModel.get_grid_origin(grid))

for opt in opts:
    print(bmiheatModel.get_var_nbytes(opt))
    print(bmiheatModel.get_var_type(opt))
    grid = bmiheatModel.get_var_grid(opt)
    print(bmiheatModel.get_grid_type(grid))
    print(bmiheatModel.get_grid_shape(grid))
    print(bmiheatModel.get_grid_spacing(grid))
    print(bmiheatModel.get_grid_origin(grid))
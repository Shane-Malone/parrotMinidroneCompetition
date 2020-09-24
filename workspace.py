import matlab.engine
eng = matlab.engine.start_matlab()
x = 4.0
eng.workspace['testin123'] = x
from data_management import Data, Calculation

print("Link Budget Tool\nADSEEII Group 22\n\n")



data = Data()
filename = input('Fill in input file:\n\t')
data.load_data(filename)

calculation1 = Calculation(input_data=data)

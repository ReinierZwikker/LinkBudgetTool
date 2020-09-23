from interface import Data

data = Data()
filename = input('Fill in input file:\n\t')
data.load_data(filename)

print(data.downlink_time_ratio)

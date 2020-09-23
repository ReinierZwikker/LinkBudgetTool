class Data:
    
    def __init__(self):

        self.orbit_height = None
        self.earth_orbit = None
        self.space_craft_sun_distance = None
        self.elongation_angle = None

        self.space_antenna_diameter = None
        self.ground_antenna_diameter = None
        self.space_pointing_offset = None
        self.ground_pointing_offset = None
        self.antenna_efficiency = None
        self.system_noise_temp = None
        self.tx_power = None
        self.tx_path_loss = None
        self.tx_loss_factor = None
        self.rx_loss_factor = None
        self.duty_cycle = None
        self.signal_frequency = None
        self.downlink_time_ratio = None
        self.generated_data_rate = None

    def load_data(self, filename):
        try:
            with open('./' + filename) as file:
                raw_data = file.read()
        except FileNotFoundError:
            try:
                with open('./' + filename + '.dat') as file:
                    raw_data = file.read()
            except FileNotFoundError:
                print('\nFile not found!')
                raise SystemExit

        raw_data += '\n'

        values = []
        comment_line = False
        current_value = ''
        value_end = False
        for char in raw_data:
            if char == '#':
                comment_line = True
            elif char == '\n':
                if not comment_line and len(current_value) > 0:
                    value_end = True
                else:
                    comment_line = False
            elif not comment_line:
                current_value += char

            if value_end:
                try:
                    values.append(float(current_value))
                except ValueError:
                    print('Please only fill in Numbers!')
                    raise SystemExit
                current_value = ''
                value_end = False

        self.orbit_height = values[0]
        self.earth_orbit = values[1]
        self.space_craft_sun_distance = values[2]
        self.elongation_angle = values[3]
        self.space_antenna_diameter = values[4]
        self.ground_antenna_diameter = values[5]
        self.space_pointing_offset = values[6]
        self.ground_pointing_offset = values[7]
        self.antenna_efficiency = values[8]
        self.system_noise_temp = values[9]
        self.tx_power = values[10]
        self.tx_path_loss = values[11]
        self.tx_loss_factor = values[12]
        self.rx_loss_factor = values[13]
        self.duty_cycle = values[14]
        self.signal_frequency = values[15]
        self.downlink_time_ratio = values[16]
        self.generated_data_rate = values[17]

class Data:

    def __init__(self):

        self.name = None

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
        self.system_noise_temp_given = None
        self.tx_power = None
        self.tx_path_loss = None
        self.tx_loss_factor = None
        self.rx_loss_factor = None
        self.duty_cycle = None
        self.signal_frequency = None
        self.downlink_time_ratio = None
        self.generated_data_rate = None
        self.generated_data_rate_given = None
        self.pixel_size = None
        self.velocity_spacecraft = None
        self.swath_width = None
        self.bits_per_pixel = None

        self.required_snr = None

        self.output = None

    def load_data(self, filename):
        self.name = filename.split('.')[0]
        try:
            with open('./' + filename) as file:
                raw_data = file.read()
        except FileNotFoundError:
            try:
                with open('./' + filename + '.dat') as file:
                    raw_data = file.read()
            except FileNotFoundError:
                print('File not found!')
                return None

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
                    pass
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
        self.system_noise_temp_given = values[10]
        self.tx_power = values[11]
        self.tx_path_loss = values[12]
        self.tx_loss_factor = values[13]
        self.rx_loss_factor = values[14]
        self.duty_cycle = values[15]
        self.signal_frequency = values[16]
        self.downlink_time_ratio = values[17]
        self.generated_data_rate = values[18]
        self.generated_data_rate_given = values[19]
        self.pixel_size = values[20]
        self.velocity_spacecraft = values[21]
        self.swath_width = values[22]
        self.bits_per_pixel = values[23]
        self.required_snr = values[24]
        return True

    def print_values(self):
        print("orbit_height " + str(self.orbit_height) + "\n" +
              "earth_orbit " + str(self.earth_orbit) + "\n" +
              "space_craft_sun_distance " + str(self.space_craft_sun_distance) + "\n" +
              "elongation_angle " + str(self.elongation_angle) + "\n" +
              "space_antenna_diameter " + str(self.space_antenna_diameter) + "\n" +
              "ground_antenna_diameter " + str(self.ground_antenna_diameter) + "\n" +
              "space_pointing_offset " + str(self.space_pointing_offset) + "\n" +
              "ground_pointing_offset " + str(self.ground_pointing_offset) + "\n" +
              "antenna_efficiency " + str(self.antenna_efficiency) + "\n" +
              "system_noise_temp  " + str(self.system_noise_temp) + "\n" +
              "system_noise_temp_given " + str(self.system_noise_temp_given) + "\n" +
              "tx_power " + str(self.tx_power) + "\n" +
              "tx_path_loss " + str(self.tx_path_loss) + "\n" +
              "tx_loss_factor " + str(self.tx_loss_factor) + "\n" +
              "rx_loss_factor " + str(self.rx_loss_factor) + "\n" +
              "duty_cycle " + str(self.duty_cycle) + "\n" +
              "signal_frequency " + str(self.signal_frequency) + "\n" +
              "downlink_time_ratio " + str(self.downlink_time_ratio) + "\n" +
              "generated_data_rate " + str(self.generated_data_rate) + "\n" +
              "generated_data_rate_given " + str(self.generated_data_rate_given) + "\n" +
              "pixel_size " + str(self.pixel_size) + "\n" +
              "velocity_spacecraft " + str(self.velocity_spacecraft) + "\n" +
              "swath_width " + str(self.swath_width) + "\n" +
              "bits_per_pixel " + str(self.bits_per_pixel) + "\n")

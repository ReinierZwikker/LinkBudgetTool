import numpy as np


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

    def set_values(self, values):
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

    def get_values(self):
        values = np.zeros(25)
        values[0] = self.orbit_height
        values[1] = self.earth_orbit
        values[2] = self.space_craft_sun_distance
        values[3] = self.elongation_angle
        values[4] = self.space_antenna_diameter
        values[5] = self.ground_antenna_diameter
        values[6] = self.space_pointing_offset
        values[7] = self.ground_pointing_offset
        values[8] = self.antenna_efficiency
        values[9] = self.system_noise_temp
        values[10] = self.system_noise_temp_given
        values[11] = self.tx_power
        values[12] = self.tx_path_loss
        values[13] = self.tx_loss_factor
        values[14] = self.rx_loss_factor
        values[15] = self.duty_cycle
        values[16] = self.signal_frequency
        values[17] = self.downlink_time_ratio
        values[18] = self.generated_data_rate
        values[19] = self.generated_data_rate_given
        values[20] = self.pixel_size
        values[21] = self.velocity_spacecraft
        values[22] = self.swath_width
        values[23] = self.bits_per_pixel
        values[24] = self.required_snr
        return values

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
        self.set_values(values)
        return True

    def print_values(self):
        print("1.  orbit height\t\t" + str(self.orbit_height) + "\n" +
              "2.  earth orbit?\t\t" + str(self.earth_orbit) + "\n" +
              "3.  space craft sun distance\t" + str(self.space_craft_sun_distance) + "\n" +
              "4.  elongation angle\t\t" + str(self.elongation_angle) + "\n" +
              "5.  space antenna diameter\t" + str(self.space_antenna_diameter) + "\n" +
              "6.  ground antenna diameter\t" + str(self.ground_antenna_diameter) + "\n" +
              "7.  space pointing offset\t" + str(self.space_pointing_offset) + "\n" +
              "8.  ground pointing offset\t" + str(self.ground_pointing_offset) + "\n" +
              "9.  antenna efficiency\t\t" + str(self.antenna_efficiency) + "\n" +
              "10. system noise temp\t\t" + str(self.system_noise_temp) + "\n" +
              "11. system noise temp given?\t" + str(self.system_noise_temp_given) + "\n" +
              "12. tx power\t\t\t" + str(self.tx_power) + "\n" +
              "13. tx path loss\t\t" + str(self.tx_path_loss) + "\n" +
              "14. tx loss factor\t\t" + str(self.tx_loss_factor) + "\n" +
              "15. rx loss factor\t\t" + str(self.rx_loss_factor) + "\n" +
              "16. duty cycle\t\t\t" + str(self.duty_cycle) + "\n" +
              "17. signal frequency\t\t" + str(self.signal_frequency) + "\n" +
              "18. downlink time ratio\t\t" + str(self.downlink_time_ratio) + "\n" +
              "19. generated data rate\t\t" + str(self.generated_data_rate) + "\n" +
              "20. generated data rate given?\t" + str(self.generated_data_rate_given) + "\n" +
              "21. pixel size\t\t\t" + str(self.pixel_size) + "\n" +
              "22. velocity spacecraft\t\t" + str(self.velocity_spacecraft) + "\n" +
              "23. swath width\t\t\t" + str(self.swath_width) + "\n" +
              "24. bits per pixel\t\t" + str(self.bits_per_pixel) + "\n" +
              "25. required SNR\t\t" + str(self.required_snr) + "\n" +
              "Boolean values?: (0=FALSE,1=TRUE)")

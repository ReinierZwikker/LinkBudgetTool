import numpy as np
from data_management import Data

au = 1.495978707e11         # m
c = 299792458               # m/s
radius_earth = 6.3781e6     # m


def get_space_loss(earth_orbit, orbit_height, space_craft_sun_distance, elongation_angle, signal_frequency):
    if earth_orbit == 1:
        max_spacecraft_distance = np.sqrt((radius_earth + orbit_height) ** 2 - radius_earth ** 2)
    else:
        max_spacecraft_distance = np.sqrt(au ** 2 + space_craft_sun_distance ** 2 - (2 * au * space_craft_sun_distance * np.cos(elongation_angle)))
    wavelength = c / signal_frequency
    space_loss_unit = (wavelength / (4 * np.pi * max_spacecraft_distance)) ** 2
    return 10 * np.log10(space_loss_unit / 1)


def get_pointing_loss(signal_frequency, space_antenna_diameter, ground_antenna_diameter, space_pointing_offset):
    half_power_angle_transmitter = 21 / ((signal_frequency / 1e9) * space_antenna_diameter)
    half_power_angle_receiver = 21 / ((signal_frequency / 1e9) * ground_antenna_diameter)
    pointing_loss_transmitter = -12 * (space_pointing_offset / half_power_angle_transmitter) ** 2
    ground_pointing_offset = half_power_angle_receiver * 0.1
    pointing_loss_reciever = -12 * (ground_pointing_offset / half_power_angle_receiver) ** 2
    return pointing_loss_transmitter + pointing_loss_reciever


def get_antenna_gain(space_antenna_diameter, ground_antenna_diameter, signal_frequency, antenna_efficiency):
    wavelength = c / signal_frequency
    transmitter_gain = 20 * np.log10(space_antenna_diameter) + 20 * np.log10(signal_frequency) + 17.8
    receiver_gain = ((np.pi ** 2) * (ground_antenna_diameter ** 2))/(wavelength ** 2) * antenna_efficiency
    return transmitter_gain, receiver_gain


def get_generated_data_rate(pixel_size, velocity_spacecraft, swath_width, bits_per_pixel):
    return bits_per_pixel * ((swath_width * velocity_spacecraft) / (pixel_size ** 2))


def get_required_data_rate_db(generated_data_rate, duty_cycle, downlink_time_ratio):
    required_data_rate_unit = generated_data_rate * duty_cycle / downlink_time_ratio
    required_data_rate_db = 1 / (10 * np.log10(1 / required_data_rate_unit))
    return required_data_rate_db


def get_transmitter_power_db(transmitter_power):
    return 10 * np.log10(transmitter_power / 1)


def get_system_noise_temperature(antenna_noise_temperature, cable_loss_factor, amplifier_noise_figure):
    return antenna_noise_temperature + 290 * ((1 - cable_loss_factor) / cable_loss_factor) + (290 * (amplifier_noise_figure - 1))


def get_system_noise_temperature_db(system_noise_temperature):
    return 1 / (10 * np.log10(1 / system_noise_temperature))


def get_recieved_snr(data):
    transmitter_power_db = get_transmitter_power_db(data.tx_power)
    transmitter_gain, reciever_gain = get_antenna_gain(data.space_antenna_diameter, data.ground_antenna_diameter, data.signal_frequency, data.antenna_efficiency)
    space_loss = get_space_loss(data.earth_orbit, data.orbit_height, data.space_craft_sun_distance, data.elongation_angle, data.signal_frequency)
    pointing_loss = get_pointing_loss(data.signal_frequency, data.space_antenna_diameter, data.ground_antenna_diameter, data.space_pointing_offset)
    if data.generated_data_rate_given == 1:
        required_data_rate = get_required_data_rate_db(data.generated_data_rate, data.duty_cycle, data.downlink_time_ratio)
    else:
        required_data_rate = get_required_data_rate_db(get_generated_data_rate(data.pixel_size, data.velocity_spacecraft, data.swath_width, data.bits_per_pixel), data.duty_cycle, data.downlink_time_ratio)
    if data.system_noise_temp_given == 1:
        system_noise_temperature = get_system_noise_temperature_db(data.system_noise_temp)
    else:
        system_noise_temperature = get_system_noise_temperature_db(get_system_noise_temperature(data.antenna_noise_temperature, data.cable_loss_factor, data.amplifier_noise_figure))
    return transmitter_power_db + data.tx_loss_factor + transmitter_gain + data.tx_path_loss + reciever_gain + space_loss + pointing_loss + data.rx_loss_factor - required_data_rate - 1.38e-23 - system_noise_temperature


# print(space_loss(True, 570000, 0, 0, 2.5e9))
# print(pointing_loss(2.5e9, 0.5, 10, 0.25))

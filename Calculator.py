import numpy as np
au = 1.495978707e11         # m
c = 299792458               # m/s
radius_earth = 6.3781e6     # m


def space_loss(earth_orbit, orbit_height, space_craft_sun_distance, elongation_angle, signal_frequency):
    if earth_orbit == 1:
        max_spacecraft_distance = np.sqrt((radius_earth + orbit_height) ** 2 - radius_earth ** 2)
    else:
        max_spacecraft_distance = np.sqrt(au ** 2 + space_craft_sun_distance ** 2 - (2 * au * space_craft_sun_distance * np.cos(elongation_angle)))
    wavelength = c / signal_frequency
    space_loss_unit = (wavelength / (4 * np.pi * max_spacecraft_distance)) ** 2
    return 10 * np.log10(space_loss_unit / 1)


def pointing_loss(signal_frequency, space_antenna_diameter, ground_antenna_diameter, space_pointing_offset):
    half_power_angle_transmitter = 21 / ((signal_frequency / 1e9) * space_antenna_diameter)
    half_power_angle_reciever = 21 / ((signal_frequency / 1e9) * ground_antenna_diameter)
    pointing_loss_transmitter = -12 * (space_pointing_offset / half_power_angle_transmitter) ** 2
    ground_pointing_offset = half_power_angle_reciever * 0.1
    pointing_loss_reciever = -12 * (ground_pointing_offset / half_power_angle_reciever) ** 2
    return pointing_loss_transmitter + pointing_loss_reciever




# print(space_loss(True, 570000, 0, 0, 2.5e9))
# print(pointing_loss(2.5e9, 0.5, 10, 0.25))

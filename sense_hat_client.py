import requests

host = 'http://hardsense:8080'


def g(action, *args):
    url = host+'/'+action
    for arg in args:
        url += '/'+str(arg)
    r = requests.get(url)
    return r.json()


def __init__(imu_settings_file, text_assets):
    return g('__init__', imu_settings_file, text_assets)['return_value']


def _load_text_assets(text_image_file, text_file):
    return g('_load_text_assets', text_image_file, text_file)['return_value']


def _trim_whitespace(char):
    return g('_trim_whitespace', char)['return_value']


def _get_settings_file(imu_settings_file):
    return g('_get_settings_file', imu_settings_file)['return_value']


def _get_fb_device():
    return g('_get_fb_device', )['return_value']


def rotation():
    return g('rotation', )['return_value']


def rotation(r):
    return g('rotation', r)['return_value']


def set_rotation(r, redraw):
    return g('set_rotation', r, redraw)['return_value']


def _pack_bin(pix):
    return g('_pack_bin', pix)['return_value']


def _unpack_bin(packed):
    return g('_unpack_bin', packed)['return_value']


def flip_h(redraw):
    return g('flip_h', redraw)['return_value']


def flip_v(redraw):
    return g('flip_v', redraw)['return_value']


def set_pixels(pixel_list):
    return g('set_pixels', pixel_list)['return_value']


def get_pixels():
    return g('get_pixels', )['return_value']


def set_pixel(x, y):
    return g('set_pixel', x, y)['return_value']


def get_pixel(x, y):
    return g('get_pixel', x, y)['return_value']


def load_image(file_path, redraw):
    return g('load_image', file_path, redraw)['return_value']


def clear():
    return g('clear', )['return_value']


def _get_char_pixels(s):
    return g('_get_char_pixels', s)['return_value']


def show_message(text_string, scroll_speed, text_colour, back_colour):
    return g('show_message', text_string, scroll_speed, text_colour, back_colour)['return_value']


def show_letter(s, text_colour, back_colour):
    return g('show_letter', s, text_colour, back_colour)['return_value']


def gamma():
    return g('gamma', )['return_value']


def gamma(buffer):
    return g('gamma', buffer)['return_value']


def gamma_reset():
    return g('gamma_reset', )['return_value']


def low_light():
    return g('low_light', )['return_value']


def low_light(value):
    return g('low_light', value)['return_value']


def _init_humidity():
    return g('_init_humidity', )['return_value']


def _init_pressure():
    return g('_init_pressure', )['return_value']


def get_humidity():
    return g('get_humidity', )['return_value']


def humidity():
    return g('humidity', )['return_value']


def get_temperature_from_humidity():
    return g('get_temperature_from_humidity', )['return_value']


def get_temperature_from_pressure():
    return g('get_temperature_from_pressure', )['return_value']


def get_temperature():
    return g('get_temperature', )['return_value']


def temp():
    return g('temp', )['return_value']


def temperature():
    return g('temperature', )['return_value']


def get_pressure():
    return g('get_pressure', )['return_value']


def pressure():
    return g('pressure', )['return_value']


def _init_imu():
    return g('_init_imu', )['return_value']


def set_imu_config(compass_enabled, gyro_enabled, accel_enabled):
    return g('set_imu_config', compass_enabled, gyro_enabled, accel_enabled)['return_value']


def _read_imu():
    return g('_read_imu', )['return_value']


def _get_raw_data(is_valid_key, data_key):
    return g('_get_raw_data', is_valid_key, data_key)['return_value']


def get_orientation_radians():
    return g('get_orientation_radians', )['return_value']


def orientation_radians():
    return g('orientation_radians', )['return_value']


def get_orientation_degrees():
    return g('get_orientation_degrees', )['return_value']


def get_orientation():
    return g('get_orientation', )['return_value']


def orientation():
    return g('orientation', )['return_value']


def get_compass():
    return g('get_compass', )['return_value']


def compass():
    return g('compass', )['return_value']


def get_compass_raw():
    return g('get_compass_raw', )['return_value']


def compass_raw():
    return g('compass_raw', )['return_value']


def get_gyroscope():
    return g('get_gyroscope', )['return_value']


def gyro():
    return g('gyro', )['return_value']


def gyroscope():
    return g('gyroscope', )['return_value']


def get_gyroscope_raw():
    return g('get_gyroscope_raw', )['return_value']


def gyro_raw():
    return g('gyro_raw', )['return_value']


def gyroscope_raw():
    return g('gyroscope_raw', )['return_value']


def get_accelerometer():
    return g('get_accelerometer', )['return_value']


def accel():
    return g('accel', )['return_value']


def accelerometer():
    return g('accelerometer', )['return_value']


def get_accelerometer_raw():
    return g('get_accelerometer_raw', )['return_value']


def accel_raw():
    return g('accel_raw', )['return_value']


def accelerometer_raw():
    return g('accelerometer_raw', )['return_value']


if __name__ == '__main__':
    pass

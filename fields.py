from modes import *

# mode_traffic
field_rate_down = 'rate_down'
#field_bw_down = 'bw_down'
field_rate_up = 'rate_up'
#field_bw_up = 'bw_up'

# mode_temp
field_cpum = 'cpum'
field_cpub = 'cpub'
field_sw = 'sw'
field_hdd = 'hdd'

# mode_fan_speed
field_fan_speed = 'fan_speed'

# mode_xdsl
field_snr_down = 'snr_down'
field_snr_up = 'snr_up'

# mode_xdsl_errors
field_fec = 'fec'
field_crc = 'crc'
field_hec = 'hec'
field_es = 'es'
field_ses = 'ses'

# mode_switch1
field_rx1 = 'rx_1'
field_tx1 = 'tx_1'
# mode_switch2
field_rx2 = 'rx_2'
field_tx2 = 'tx_2'
# mode_switch3
field_rx3 = 'rx_3'
field_tx3 = 'tx_3'
# mode_switch4
field_rx4 = 'rx_4'
field_tx4 = 'tx_4'
# mode_switch5
field_rx5 = 'rx_5'
field_tx5 = 'tx_5'

# mode_transmission_tasks
field_nb_tasks_stopped = 'nb_tasks_stopped'
field_nb_tasks_checking = 'nb_tasks_checking'
field_nb_tasks_queued = 'nb_tasks_queued'
field_nb_tasks_extracting = 'nb_tasks_extracting'
field_nb_tasks_done = 'nb_tasks_done'
field_nb_tasks_repairing = 'nb_tasks_repairing'
field_nb_tasks_downloading = 'nb_tasks_downloading'
field_nb_tasks_error = 'nb_tasks_error'
field_nb_tasks_stopping = 'nb_tasks_stopping'
field_nb_tasks_seeding = 'nb_tasks_seeding'
# field_nb_tasks_active = 'nb_tasks_active'  # Total active
# nb_tasks = 'nb_tasks'  # Total

# mode_transmission_rate
field_rx_throttling = 'throttling_rate.rx_rate'
field_tx_throttling = 'throttling_rate.tx_rate'
field_rx_rate = 'rx_rate'
field_tx_rate = 'tx_rate'

# mode connection
field_bytes_up = 'bytes_up'
field_bytes_down = 'bytes_down'

# mode ftth
field_has_sfp = 'has_sfp'
field_link = 'link'
field_sfp_alim_ok = 'sfp_alim_ok'
field_sfp_has_signal = 'sfp_has_signal'
field_sfp_present = 'sfp_present'

# mode switch-bytes
field_rx_bytes = 'rx_good_bytes'
field_tx_bytes = 'tx_bytes'

# mode switch-packets
field_rx_packets = 'rx_good_packets'
field_tx_packets = 'tx_packets'
field_rx_unicast_packets = 'rx_unicast_packets'
field_tx_unicast_packets = 'tx_unicast_packets'
field_rx_broadcast_packets = 'rx_broadcast_packets'
field_tx_broadcast_packets = 'tx_broadcast_packets'

# mode wifi-stations
field_stations = 'stations'

# mode wifi-bytes
field_wifi_rx_bytes = 'rx_bytes'
field_wifi_tx_bytes = 'tx_bytes'

fields = {
    mode_traffic: [
        field_rate_down,
#        field_bw_down,
        field_rate_up,
#        field_bw_up
    ],
    mode_temp: [
        field_cpum,
        field_cpub,
        field_sw,
        field_hdd
    ],
    mode_fan_speed: [
        field_fan_speed
    ],
    mode_xdsl: [
        field_snr_down,
        field_snr_up
    ],
    mode_xdsl_errors: [
        field_fec,
        field_crc,
        field_hec,
        field_es,
        field_ses
    ],
    mode_switch1: [
        field_rx1,
        field_tx1
    ],
    mode_switch2: [
        field_rx2,
        field_tx2
    ],
    mode_switch3: [
        field_rx3,
        field_tx3
    ],
    mode_switch4: [
        field_rx4,
        field_tx4
    ],
    mode_switch5: [
        field_rx5,
        field_tx5
    ],
    mode_switch_bytes: [
        field_rx_bytes,
        field_tx_bytes,
    ],
    mode_switch_packets: [
        field_rx_packets,
        field_tx_packets,
        field_rx_unicast_packets,
        field_tx_unicast_packets,
        field_rx_broadcast_packets,
        field_tx_broadcast_packets,
    ],
    mode_transmission_tasks: [
        field_nb_tasks_stopped,
        field_nb_tasks_checking,
        field_nb_tasks_queued,
        field_nb_tasks_extracting,
        field_nb_tasks_done,
        field_nb_tasks_repairing,
        field_nb_tasks_downloading,
        field_nb_tasks_error,
        field_nb_tasks_stopping,
        field_nb_tasks_seeding
    ],
    mode_transmission_traffic: [
        field_rx_throttling,
        field_tx_throttling,
        field_rx_rate,
        field_tx_rate,
    ],
    mode_connection: [
        field_bytes_up,
        field_bytes_down,
    ],
    mode_connection_log: [
        field_bytes_up,
        field_bytes_down,
    ],
    mode_ftth: [
        field_has_sfp,
        field_link,
        field_sfp_alim_ok,
        field_sfp_has_signal,
        field_sfp_present,
    ],
    mode_wifi_stations: [
        field_stations,
    ],
    mode_wifi_bytes: [
        field_wifi_rx_bytes,
        field_wifi_tx_bytes,
    ],
    mode_wifi_bytes_log: [
        field_wifi_rx_bytes,
        field_wifi_tx_bytes,
    ],
}

xdsl_errors_fields_descriptions = {
    field_fec: 'FEC (Forward Error Connection)',
    field_crc: 'CRC (Cyclic Redundancy Check)',
    field_hec: 'HEC (Header Error Control)',
    field_es: 'ES (Errored Seconds)',
    field_ses: 'SES (Severely Errored Seconds)'
}


def get_fields(mode):
    if mode not in fields:
        print('Unknown mode {}'.format(mode))

    return fields[mode]

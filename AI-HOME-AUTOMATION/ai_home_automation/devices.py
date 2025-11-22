devices = {
    "light": False,
    "fan": False,
    "ac": False,
    "door": False
}

def toggle_device(device, state):
    if device in devices:
        devices[device] = state
        return True
    return False

def get_device_states():
    return devices

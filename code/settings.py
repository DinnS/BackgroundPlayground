from win32api import GetSystemMetrics

# GLOBAL SETTINGS

# Current screen size (Full screen)
SCREEN_WIDTH = GetSystemMetrics(0)
SCREEN_HEIGHT = GetSystemMetrics(1)
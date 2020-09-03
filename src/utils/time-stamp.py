import pendulum
from Config.config as ENV


def get_timestamp():
    return str(pendulum.now(ENV.TIME_ZONE))


from __future__ import print_function

import napalm
import sys
import os


def main(config_file):
    """Load a config for the device."""

    if not (os.path.exists(config_file) and os.path.isfile(config_file)):
        msg = "Missing or invalid config file {0}".format(config_file)
        raise ValueError(msg)

    print("Loading config file {0}.".format(config_file))

    # Use the appropriate network driver to connect to the device:
    driver = napalm.get_network_driver("ios")

    # Connect:
    device = driver(
        hostname="siteA.vd.com",
        username="cisco",
        password="cisco123",
        optional_args={"port": 22},
    )

    print("Opening ...")
    device.open()

    print("Loading replacement candidate ...")
    device.load_replace_candidate(filename=config_file)

    # Note that the changes have not been applied yet. Before applying
    # the configuration you can check the changes:
    print("\nDiff:")
    print(device.compare_config())

    # You can commit or discard the candidate changes.
    try:
        choice = input("\nWould you like to commit these changes? [yN]: ")
    except NameError:
        choice = input("\nWould you like to commit these changes? [yN]: ")
    if choice == "y":
        print("Committing ...")
        device.commit_config()
    else:
        print("Discarding ...")
        device.discard_config()

    # close the session with the device.
    device.close()
    print("Done.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please supply the full path to "new_good.conf"')
        sys.exit(1)
    config_file = sys.argv[1]
    main(config_file)

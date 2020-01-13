from pymavlink import mavutil
import time

def main():
    master = mavutil.mavlink_connection('udp:test-script:14551')

    print("waiting")
    master.wait_heartbeat()
    mode = mavutil.mavlink.MAV_MOUNT_MODE_MAVLINK_TARGETING
    master.mav.mount_configure_send(master.target_system,
                                    master.target_component,
                                    mode,
                                    1, 1, 1)
    time.sleep(1)
    master.mav.mount_control_send(master.target_system, 
                                  master.target_component, 
                                  -2000, 
                                  -2000,
                                   0, 0)
    print("Sent Command")

    while True:
        print(master.recv_match().to_dict())
        time.sleep(0.01)

if __name__ == "__main__":
    main()

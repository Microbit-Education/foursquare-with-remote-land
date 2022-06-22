def on_button_pressed_a():
    basic.pause(5000)
    Drones.Basic_action(Drones.Basicoptions.TAKEOFF)
    Drones.Move_action(Drones.Directionoptions.FORWARD, 100)
    Drones.Move_action(Drones.Directionoptions.RIGHT, 100)
    Drones.Move_action(Drones.Directionoptions.BACKWARD, 100)
    Drones.Move_action(Drones.Directionoptions.LEFT, 100)
    Drones.hovering(1)
    Drones.Basic_action(Drones.Basicoptions.LANDING)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    if receivedString == "stop":
        basic.show_icon(IconNames.SAD)
        Drones.Basic_action(Drones.Basicoptions.LANDING)
        basic.show_icon(IconNames.SWORD)
        control.reset()
radio.on_received_string(on_received_string)

basic.show_icon(IconNames.SQUARE)
radio.set_group(33)
Drones.init_module(Drones.Runmodes.MASTER)
basic.show_icon(IconNames.YES)
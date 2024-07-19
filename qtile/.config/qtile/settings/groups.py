import os
import subprocess
from libqtile import hook, bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List
from .keys import mod, keys
from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupImage,
    PopupText,
    PopupWidget
)

# Global variable to keep track of the current popup
current_popup = None

# Function to show the popup with group information
def show_graphs(qtile):
    global current_popup

    # Hide the current popup if it exists
    if current_popup:
        current_popup.hide()
        current_popup = None

    # Configuration for the GroupBox widget
    group_box_config = {
        "active": "#5165e7",
        "border_width": "1",
        "disable_drag": True,
        "fontsize": 20,
        "highlight_method": "text",
        "inactive": "#ffffff",
        "margin_x": 5,
        "margin_y": 5,
        "this_current_screen_border": "#fff421",
        "this_screen_border": "#ffffff",
        "urgent_alert_method": "text",
        "urgent_border": "#ffffff",
        "padding": 0,
    }

    # Define the controls for the popup, including the GroupBox widget
    controls = [
        PopupWidget(
            widget=widget.GroupBox(**group_box_config),
            width=1.5,
            height=0.45,
            pos_x=0.05,
            pos_y=0.25
        ),
    ]

    # Configuration for the PopupRelativeLayout
    layout_config = {
        "qtile": qtile,
        "width": 250,
        "padding": 0,
        "height": 50,
        "margin": 0,
        "controls": controls,
        "background": "00000060",
        "initial_focus": None,
        "close_on_click": True,
    }

    # Create and show the popup layout
    current_popup = PopupRelativeLayout(**layout_config)
    current_popup.show(835, 875)
    # Schedule the popup to hide after 1.5 seconds
    qtile.call_later(1.5, current_popup.hide)

# Function to create groups with specified names, labels, and layouts
def create_groups():
    group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    group_labels = ["󰣇", "󰮯", "\uf444", "\uf444", "󰊠", "\uf444", "\uf444", "\uf444", "󰊠"]
    group_layouts = ["columns"] * 9

    # Create a list of Group objects
    return [Group(name=group_names[i], layout=group_layouts[i], label=group_labels[i]) for i in range(len(group_names))]

# Function to switch to a specified group and show the popup
def switch_to_group_with_popup(qtile, group_name):
    qtile.cmd_spawn(f"xdotool key {mod}+{group_name}")
    show_graphs(qtile)

# Function to configure key bindings for groups
def configure_keys(groups):
    for group in groups:
        keys.extend([
            # Bind key to switch to the group
            Key(
                [mod],
                group.name,
                lazy.group[group.name].toscreen(),
                lazy.function(switch_to_group_with_popup, group.name),
                desc=f"Switch to group {group.name}"
            ),
            # Bind key to move focused window to the group
            Key(
                [mod, "shift"],
                group.name,
                lazy.window.togroup(group.name, switch_group=False),
                desc=f"Move focused window to group {group.name}"
            ),
        ])

# Create the groups
groups = create_groups()
# Configure the key bindings for the groups
configure_keys(groups)

import os
import re
import socket
import subprocess
from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook, qtile, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule
from libqtile.command import lazy
from libqtile.widget import Spacer
from libqtile.dgroups import simple_key_binder


# Globals
MOD = "mod4"
ALT_KEY = "mod1"
TERMINAL = "alacritty"
BROWSER = "firefox"
FILE_MANAGER = "thunar"

# Key Bindings
keys = [
    Key([MOD], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([MOD], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([MOD], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([MOD], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([MOD], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([MOD], "j", lazy.layout.down(), desc="Move focus down"),
    Key([MOD], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([MOD], "k", lazy.layout.up(), desc="Move focus up"),
    Key([MOD], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key(
        [MOD, "shift"],
        "Down",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [MOD, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [MOD, "shift"],
        "Up",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc="Move windows up in current stack",
    ),
    Key(
        [MOD, "shift"],
        "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc="Move windows up in current stack",
    ),
    Key(
        [MOD, "shift"],
        "space",
        lazy.layout.flip(),
        desc="Flip windows in current stack",
    ),
    Key([MOD, "shift"], "Left", lazy.screen.prev_group(), desc="Move to group on left"),
    Key([MOD, "shift"], "h", lazy.screen.prev_group(), desc="Move to group on left"),
    Key(
        [MOD, "shift"], "Right", lazy.screen.next_group(), desc="Move to group on right"
    ),
    Key([MOD, "shift"], "l", lazy.screen.next_group(), desc="Move to group on right"),
    Key([MOD, ALT_KEY], "Left", lazy.to_screen(0), desc="Move to screen on left"),
    Key([MOD, ALT_KEY], "h", lazy.to_screen(0), desc="Move to screen on left"),
    Key([MOD, ALT_KEY], "Right", lazy.to_screen(1), desc="Move to screen on right"),
    Key([MOD, ALT_KEY], "l", lazy.to_screen(1), desc="Move to screen on right"),
    Key([ALT_KEY], "Tab", lazy.screen.next_group(), desc="Move to group on right"),
    Key(
        [MOD, "control"],
        "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [MOD, "control"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [MOD, "control"],
        "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key(
        [MOD, "control"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([MOD, "control"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([MOD, "control"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([MOD, "control"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([MOD, "control"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([MOD], "Return", lazy.spawn(TERMINAL), desc="Launch terminal"),
    Key([MOD], "b", lazy.spawn(BROWSER), desc="Launch browser"),
    Key([MOD], "f", lazy.spawn(FILE_MANAGER), desc="Launch file manager"),
    Key([MOD], "v", lazy.spawn("pavucontrol"), desc="Launch audio manager interface"),
    Key([MOD], "e", lazy.spawn("emacsclient -c -a 'emacs' "), desc="Launch Emacs"),
    Key(
        [MOD],
        "r",
        lazy.run_extension(
            extension.DmenuRun(
                dmenu_prompt=">",
                dmenu_font="Andika-18",
                background="#15181a",
                foreground="#00ff00",
                selected_background="#079822",
                selected_foreground="#fff",
            )
        ),
    ),
    Key([MOD], "q", lazy.window.kill(), desc="Kill active window"),
    Key([MOD, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([MOD, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

layout_theme = {
    "margin": 5,
    "border_focus": "#fba922",
    "border_normal": "#4c566a",
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme),
]


# Groups/Workspaces
groups = [
    Group(" ", layout="monadtall"),
    Group(" ", layout="monadtall"),
    Group(" ", layout="monadtall"),
    Group(" ", layout="monadtall"),
    Group(" ", layout="monadtall"),
    Group(" ", layout="monadtall"),
]
dgroups_key_binder = simple_key_binder(MOD)

widget_defaults = dict(
    font="Andika",
    fontsize=14,
    padding=2,
)

extension_defaults = widget_defaults.copy()

color_active = "#6790eb"
color_warn = "#fba922"
color_crit = "#cd1f3f"
color_ok = "#309e17"
color_diff = "#b51c8c"

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(linewidth=0, padding=6),
                widget.Image(
                    filename="~/.config/qtile/icons/gnu_icon_48.png",
                    scale="False",
                    margin_x=9,
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(
                            f"{TERMINAL} --hold -e cat /home/james/.config/qtile/extra/text.txt"
                        )
                    },
                ),
                widget.GroupBox(
                    font="FontAwesome",
                    fontsize=18,
                    margin_x=0,
                    padding_y=6,
                    padding_x=5,
                    disable_drag=True,
                    highlight_method="text",
                    this_current_screen_border=color_active,
                ),
                widget.Sep(linewidth=0, padding=10),
                widget.WindowName(
                    font="Noto Sans Bold",
                    fontsize=12,
                    foreground=color_warn,
                ),
                widget.Spacer(),
                widget.TextBox(
                    font="FontAwesome",
                    fmt=" ",
                    foreground=color_active,
                ),
                widget.CPU(
                    font="FontAwesome",
                    format="{load_percent}%",
                    foreground=color_ok,
                ),
                widget.ThermalZone(
                    font="FontAwesome",
                    foreground=color_ok,
                    fgcolor_normal=color_ok,
                    fgcolor_high=color_warn,
                    fgcolor_crit=color_crit,
                    fmt="({})",
                    crit=80,
                    high=70,
                    padding=5,
                    zone="/sys/class/hwmon/hwmon4/temp1_input",
                ),
                widget.TextBox(
                    font="FontAwesome",
                    fmt="   ",
                    foreground=color_active,
                ),
                widget.Memory(
                    font="FontAwesome",
                    fmt="{}",
                    foreground=color_ok,
                    padding=5,
                ),
                widget.TextBox(
                    font="FontAwesome",
                    fmt="  ",
                    foreground=color_active,
                ),
                widget.Net(
                    font="FontAwesome",
                    interface="enp0s25",
                    format="{down}{down_suffix} ↓↑ {up}{up_suffix}",
                    foreground=color_ok,
                    padding=5,
                ),
                widget.TextBox(
                    font="FontAwesome",
                    text="  ",
                    foreground=color_active,
                    padding=0,
                    fontsize=16,
                ),
                widget.Clock(
                    font="Noto Sans Bold",
                    foreground=color_ok,
                    fontsize=12,
                    format="%Y-%m-%d %H:%M",
                ),
                widget.CurrentLayout(
                    fmt="   Layout: {}",
                    font="Noto Sans Bold",
                    fontsize=10,
                    margin=4,
                    foreground=color_warn,
                ),
                widget.Sep(linewidth=0, padding=20),
            ],
            40,
            border_width=[0, 0, 2, 0],  # Draw bottom borders
            border_color=[
                "00ffff",
                "000000",
                "00ffff",
                "000000",
            ],
        ),
    )
]

# Drag floating layouts.
mouse = [
    Drag(
        [MOD],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [MOD], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([MOD], "Button2", lazy.window.bring_to_front()),
]

dgroups_app_rules = []

main = None


# hides the top bar when the archlinux-logout widget is opened
@hook.subscribe.client_new
def new_client(window):
    if window.name == "ArchLinux Logout":
        qtile.hide_show_bar()


# shows the top bar when the archlinux-logout widget is closed
@hook.subscribe.client_killed
def logout_killed(window):
    if window.name == "ArchLinux Logout":
        qtile.hide_show_bar()


# @hook.subscribe.startup_once
# def start_once():
#     home = os.path.expanduser("~")
#     subprocess.call([home + "/.config/qtile/scripts/autostart.sh"])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])


@hook.subscribe.client_new
def set_floating(window):
    if (
        window.window.get_wm_transient_for()
        or window.window.get_wm_type() in floating_types
    ):
        window.floating = True


floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="Arcolinux-welcome-app.py"),
        Match(wm_class="Arcolinux-calamares-tool.py"),
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="Arandr"),
        Match(wm_class="feh"),
        Match(wm_class="Galculator"),
        Match(wm_class="archlinux-logout"),
        Match(wm_class="xfce4-terminal"),
    ],
    fullscreen_border_width=0,
    border_width=0,
)
auto_fullscreen = True

focus_on_window_activation = "focus"  # or smart

wmname = "LG4D"
# Commands on start
os.system("picom &")
os.system("nitrogen --restore")

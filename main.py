import importlib
import random
import os

all_effects = effects = [
    "Beams",
    "BinaryPath",
    "Blackhole",
    "BouncyBalls",
    "Bubbles",
    "Burn",
    "ColorShift",
    "Crumble",
    "Decrypt",
    "ErrorCorrect",
    "Expand",
    "Fireworks",
    "Highlight",
    "LaserEtch",
    "Matrix",
    "MiddleOut",
    "OrbittingVolley",
    "Overflow",
    "Pour",
    "Print",
    "Rain",
    "Random Sequence",
    "Rings",
    "Scattered",
    "Slice",
    "Slide",
    "Spotlights",
    "Spray",
    "Swarm",
    "Sweep",
    "SynthGrid",
    "Unstable",
    "VHSTape",
    "Waves",
    "Wipe",
]

with open("logo.txt", "r") as file:
    logo = file.read()
try:
    while True:
        random.shuffle(all_effects)
        for effect_name in all_effects:
            os.system("clear")
            module_path = f"terminaltexteffects.effects.effect_{"_".join(effect_name.lower().split())}"
            current_module = importlib.import_module(module_path)
            effect_class = getattr(current_module, "".join(effect_name.split()))
            current_effect = effect_class(logo)
            current_effect.terminal_config.canvas_width = 0
            current_effect.terminal_config.canvas_height = 0
            current_effect.terminal_config.anchor_text = "c"
            with current_effect.terminal_output() as terminal:
                for frame in current_effect:
                    terminal.print(frame)
except KeyboardInterrupt:
    os.system("clear")
    print("Screensaver stopped !")

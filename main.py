import importlib

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

for effect_name in all_effects:
    module_path = (
        f"terminaltexteffects.effects.effect_{"_".join(effect_name.lower().split())}"
    )
    current_module = importlib.import_module(module_path)
    effect_class = getattr(current_module, "".join(effect_name.split()))
    current_effect = effect_class(logo)
    with current_effect.terminal_output() as terminal:
        for frame in current_effect:
            terminal.print(frame)

import os
import re
import shutil
from tqdm import tqdm

dir = "./Donald_Duck/"
destdir = "./Donald_Duck_Pockets/"

if not os.path.isdir(destdir):
    os.mkdir(destdir)

files = os.listdir(dir)

class ComicItem:
    def __init__(self, number, name, filepath, prop: str | None):
        self.number: str = number
        self.name: str = name
        self.filepath: str = filepath
        self.prop: str | None = prop

    def __repr__(self):
        return f"'{self.number} - {self.name}' at '{self.filepath}' with prop '{self.prop}'"

items: dict[str, list[ComicItem]] = {}

for file in files:
    sections = file.split(" - ")
    filepath = os.path.join(dir, file)

    if len(sections) != 3:
        raise ValueError("Not three sections!")

    title = sections[0]
    number = sections[1]
    number = number.replace(",", ".")
    name = sections[2]

    if name[-4:] != ".cbr":
        print(f"{file} is not of type .cbr.")

    name = name[:-4]

    prop_pattern = r"\((.*?)\)"
    props = re.findall(prop_pattern, name)
    name = re.sub(prop_pattern, "", name)
    name = name.strip()

    if len(props) == 0:
        props = None
    elif len(props) == 1:
        props = props[0]
    else:
        raise ValueError("No more props expected than 1.")

    item = ComicItem(number, name, filepath, props)

    if number not in items:
        items[number] = [item]
    else:
        items[number].append(item)

total_items = len(items)
pbar = tqdm(total=total_items)

for number, files in items.items():
    chosen_file = None
    if len(files) == 1:
        chosen_file = files[0]
    else:
        for file in files:
            if file.prop is None:
                if not chosen_file:
                    chosen_file = file
            elif file.prop.lower() == "bewerkt":
                chosen_file = file
            elif file.prop.lower() == "andere scan" and chosen_file != "Bewerkt":
                chosen_file = file
            else:
                chosen_file = files[0]

    if not chosen_file:
        raise ValueError("No comic item was chosen")

    newpath = os.path.join(destdir, f"Donald Duck Pockets {chosen_file.number} - {chosen_file.name}.cbr")
    shutil.copyfile(chosen_file.filepath, newpath)
    pbar.update(1)
pbar.close()



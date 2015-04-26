#!/usr/bin/env python
import random
import sys

"""
Takes a string containing {sections} to be replaced. Replaces them until no
braces are left in the string.

Optionally takes an argument to use as seed, for assigning results to things.
Argument can be any string, most likely a name.
"""

#string = '{title} of {adj} {discipline}'
string = '{artifact_type} of {group}'


if len(sys.argv) > 1:
    random.seed(sys.argv[1])

adjectives = [
    'Inner', 'Outer', 'Middle', 'Upper', 'Lower',
    'Northern', 'Southern', 'Eastern', 'Western',
    'Recent', 'Ancient', 'Future',
    'Applied', 'Theoretical', 'Imaginary', 'Impossible',
    'Friendly', 'Savage', 'Vindictive',
    'Invisible', 'Indefinite', 'Inadvisable', 'Oblique', 'Extreme', 'Battle', 'Infected',
]
nouns = [
    'Bandits', 'Bikers', 'Raiders', 'Guardians', 'Legion', 'Orcs',
    'Savages', 'Wizards', 'Clan', 'Zombies', 'Merchants', 'Army', 'Guild',
    'Followers of {adj} {discipline}',
]
languages = [
    'English', 'Spanish', 'Russian', 'German', 'French'
]
disciplines = [
    'Communications', 'Science', 'Bibliomancy', 'Astronomy', 'Horticulture',
    'Geography', 'Magic',
    'Computer {discipline}',
    '{language}',
]
titles = [
    'Chair', 'Dean', 'Professor', 'Lecturer',
    '{title_adj} {title}',
]
title_adjs = [
    'Senior', 'Junior', 'Assistant',
]
artifact_types = [
    'Tablet', 'Device', 'Scrolls', 'Remains', 'Casket', 'Ark', 'Journals',
    'Totem', 'Icon', 'Idol',
]
groups = [
    'the {adj} {thing}',
    'the Order of {adj} {thing}',
]

while '{' in string:
    values = dict(
        discipline = random.choice(disciplines),
        language = random.choice(languages),
        adj = random.choice(adjectives),
        title = random.choice(titles),
        title_adj = random.choice(title_adjs),
        artifact_type = random.choice(artifact_types),
        thing = random.choice(nouns),
        group = random.choice(groups),
    )
    string = string.format(**values)

print(string)

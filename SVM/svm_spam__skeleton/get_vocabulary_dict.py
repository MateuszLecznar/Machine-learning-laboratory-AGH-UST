#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv

from typing import Dict


def get_vocabulary_dict() -> Dict[int, str]:
    """Read the fixed vocabulary list from the datafile and return.

    :return: a dictionary of words mapped to their indexes
    """
    dict_voc = {}
    with open('data/vocab.txt', encoding="utf-8") as f:
        read_data = f.readlines()
        for line in read_data:
            line = line.split()
            temp_dict = {int(line[0]): line[1]}
            dict_voc.update(temp_dict)
    f.closed
    return dict_voc





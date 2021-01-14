# -*- coding: utf-8 -*-
import re


def read_data(dest_: str):
    archive = open(file=dest_, mode="r")
    data = {}
    rows = archive.readlines()
    subject_regex = re.compile(pattern=r"^[\w -]+ - [\w -]+")
    time_regex = re.compile(pattern=r"\d\d:\d\d - \d\d:\d\d$")
    day_regex = re.compile(pattern=r"^\w+$")

    for row_ in rows:
        if day_regex.match(row_):
            day = day_regex.findall(row_)[0].title()
            if day not in data:
                data[day] = {}

        if subject_regex.match(row_):
            subject = subject_regex.findall(row_)[0]
            subject = subject.split("-")[0].rstrip()
            if subject not in data[day]:
                data[day][subject] = []

        time = time_regex.findall(row_)
        if len(time) > 0:
            time = time[0]
            data[day][subject].append(time)

    return data

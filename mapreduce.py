# coding: utf-8
import collections

shuffle = collections.defaultdict(list)


def emit(key, value):
    shuffle[key].append(value)


def perform(mapper, reducer, original_dataset, spliter=lambda x: x):
    dataset = spliter(original_dataset)
    map(mapper, dataset)
    # Isso geralmente é uma base de dados
    result = {}
    for key, mapped_list in shuffle.iteritems():
        reducer(key, mapped_list, result)
    return result

import mapreduce

dataset = "Deer Bear River Car car River\nDeer Car bear\n"


def mapper(data):
    mapreduce.emit(data.strip(), 1)
    # mapreduce.emit(data.strip().lower(), 1)
    # mapreduce.emit(len(data.strip()), 1)


def reducer(key, mapped_list, result):
    result[key] = sum(mapped_list)


def spliter(data):
    return data.split()


print mapreduce.perform(mapper, reducer, dataset, spliter)

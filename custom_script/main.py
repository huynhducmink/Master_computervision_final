if __name__ == '__main__':
    from multiprocessing import Pool, cpu_count
    from os import listdir
    from os.path import join
    import json
    from worker import prepare_directories, handle_image, IMAGES_DIRECTORY, LABEL_IMAGES_DIRECTORY

    prepare_directories()

    pool = Pool(cpu_count())
    image_ids = [item[:-5] for item in listdir(IMAGES_DIRECTORY)]
    colors_to_label_names = dict()
    for result in pool.imap_unordered(handle_image, image_ids):
        for item in result:
            colors_to_label_names[item] = result[item]

    with open(join(LABEL_IMAGES_DIRECTORY, '__colors_2_labels__.json'), 'w') as label_file:
        json.dump(colors_to_label_names, label_file)

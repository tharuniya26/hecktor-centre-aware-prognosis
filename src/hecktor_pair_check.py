from pathlib import Path


def main():
    images_dir = Path("data/raw/imagesTr")
    labels_dir = Path("data/raw/labelsTr")

    image_files = sorted(images_dir.glob("*"))
    label_files = sorted(labels_dir.glob("*"))

    print("Image files:", len(image_files))
    print("Label files:", len(label_files))

    image_names = {f.stem for f in image_files}
    label_names = {f.stem for f in label_files}

    missing_labels = image_names - label_names
    missing_images = label_names - image_names

    print("Images without matching labels:", len(missing_labels))
    print("Labels without matching images:", len(missing_images))

    if missing_labels:
        print("Example missing labels:", list(missing_labels)[:5])

    if missing_images:
        print("Example missing images:", list(missing_images)[:5])


if __name__ == "__main__":
    main()
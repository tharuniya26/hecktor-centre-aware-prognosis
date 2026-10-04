from pathlib import Path


def main():
    images_dir = Path("data/raw/imagesTr")
    labels_dir = Path("data/raw/labelsTr")

    image_files = list(images_dir.iterdir()) if images_dir.exists() else []
    label_files = list(labels_dir.iterdir()) if labels_dir.exists() else []

    print("Images folder exists:", images_dir.exists())
    print("Labels folder exists:", labels_dir.exists())

    print("Number of image files:", len(image_files))
    print("Number of label files:", len(label_files))

    if len(image_files) == 0:
        print("No real HECKTOR images found yet.")

    if len(label_files) == 0:
        print("No real HECKTOR labels found yet.")


if __name__ == "__main__":
    main()
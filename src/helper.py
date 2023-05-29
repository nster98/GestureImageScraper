import os
import requests
import face_recognition


def create_folder(images):
    parent_dir = f"C:/Users/{os.getlogin()}/OneDrive/Pictures/"
    try:
        path = os.path.join(parent_dir, 'Gestures')
        os.mkdir(path)
    except FileExistsError:
        path = os.path.join(parent_dir, 'Gestures')

    download_images(images, path)


def download_images(images, folder_name):
    # initial count is zero
    count = 0

    # print total images found in URL
    print(f"Total {len(images)} Image Found!")

    # checking if images is not zero
    if len(images) != 0:
        for i, image in enumerate(images):
            image_link = image.attrs['src']

            try:
                if "https:" not in image_link:
                    image_link = 'https:' + image_link
                r = requests.get(image_link).content
                try:
                    r = str(r, 'utf-8')
                except UnicodeDecodeError:
                    image_dir = f"{folder_name}/{image.attrs['alt']}{i + 1}.jpg"
                    with open(image_dir, "wb+") as f:
                        f.write(r)

                    if not check_face(image_dir):
                        os.remove(image_dir)
                        continue

                    count += 1
            except:
                pass

        # There might be possible, that all
        # images not download
        # if all images download
        if count == len(images):
            print("All Images Downloaded!")

        # if all images not download
        else:
            print(f"Total {count} Images Downloaded Out of {len(images)}")


def check_face(image):
    face = face_recognition.load_image_file(image)
    face_locations = face_recognition.face_locations(face)

    if len(face_locations) == 0:
        return False

    return True
